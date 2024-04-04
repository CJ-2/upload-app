# Flask File Upload App

This Flask application provides a simple interface for uploading and viewing files. It supports a variety of file types including text, images, videos, and PDFs.

## Features

- File upload through a web interface.
- Support for multiple file types: txt, pdf, png, jpg, jpeg, gif, mp4, mov, avi.
- Secure filename processing.
- File listing for uploaded files.

## Installation

To run this application, you will need Python and Flask. Follow these steps to get it up and running:

1. Clone this repository or download the source code.
2. Install Flask if you haven't already.
You can install it using pip: pip install Flask
3. Navigate to the directory containing the application.
4. Run the application: python main.py

The application will start running on `http://localhost:5000`.

## Usage

- **Uploading Files:**
  - Navigate to `http://localhost:5000` in your web browser.
  - Use the upload form to select and upload a file. Only files with the allowed extensions can be uploaded.

- **Viewing Uploaded Files:**
  - After uploading, you will be redirected to the file's URL.
  - To see a list of all uploaded files, navigate to `http://localhost:5000/explore`.

## Configuration

- The upload folder and allowed file extensions can be configured in `main.py`.
- The application's port and debug mode can also be adjusted in the `if __name__ == '__main__':` block at the end of `main.py`.

## Security

This application uses `werkzeug.utils.secure_filename` to secure file names before saving them. It's important to ensure that your deployment environment is secure, as this application does not implement authentication or more advanced security features.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
