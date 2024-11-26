from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Path to the CDN folder
CDN_FOLDER = os.path.join(os.getcwd(), "cdn")

@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    try:
        # Serve files from the CDN directory
        return send_from_directory(CDN_FOLDER, filename)
    except FileNotFoundError:
        abort(404)  # Return a 404 if the file is not found

if __name__ == '__main__':
    app.run(port=3000, debug=True)
