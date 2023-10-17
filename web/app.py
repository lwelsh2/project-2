import os
from flask import Flask, send_file, abort
import configparser

app = Flask(__name__)

# Define the path to the pages directory
pages_dir = os.path.join(os.path.dirname(__file__), "pages")

# Load configuration from credentials.ini or default.ini
config = configparser.ConfigParser()
config.read(['credentials.ini', 'default.ini'])

# Get the port and debug mode
port = int(config.get('server', 'port'))
debug = config.getboolean('server', 'debug')

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/<path:filename>")
def serve_file(filename):
    file_path = os.path.join(pages_dir, filename)
    
    # Check if the file exists
    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        abort(404)  # File not found

@app.errorhandler(404)
def page_not_found(e):
    return send_file(os.path.join(pages_dir, "404.html")), 404

@app.errorhandler(403)
def forbidden(e):
    return send_file(os.path.join(pages_dir, "403.html")), 403

if __name__ == "__main__":
    app.run(debug=debug, host='0.0.0.0', port=port)
