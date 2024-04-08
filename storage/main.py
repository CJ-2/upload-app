from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from google.cloud import storage

app = Flask(__name__)

# Configure Google Cloud Storage
bucket_name = "your-bucket-name"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        blob = bucket.blob(filename)
        blob.upload_from_string(
            file.read(),
            content_type=file.content_type
        )
        return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    blob = bucket.blob(filename)
    url = blob.public_url
    if not url:
        return "File not found", 404
    return redirect(url)

@app.route('/explore')
def explore():
    files = [blob.name for blob in bucket.list_blobs()]
    return render_template('explore.html', files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
