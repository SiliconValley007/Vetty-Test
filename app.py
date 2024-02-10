from flask import Flask, render_template, request
from file_handling import FILE_HANDLING

app = Flask(__name__)


# application details option 3: filename as optional and defaults to file1.txt
@app.route("/", defaults={"filename": "file1.txt"})
@app.route("/<filename>", methods=["GET"])
def readFile(filename):
    start = request.args.get("startline", default=0, type=int)
    end = request.args.get("endline", default=0, type=int)
    file_exists = FILE_HANDLING._valid_file(filename)
    if file_exists is True:
        temp = FILE_HANDLING._read_file(filename, start, end)
