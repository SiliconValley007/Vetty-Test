from flask import Flask, render_template, request
from file_handling import FILE_HANDLING

app = Flask(__name__)
file_handling = FILE_HANDLING()


# application details option 3: filename as optional and defaults to file1.txt
@app.route("/", defaults={"filename": "file1.txt"})
@app.route("/<filename>", methods=["GET"])
def readFile(filename):
    start = request.args.get("startline", default=0, type=int)
    end = request.args.get("endline", default=0, type=int)
    file_exists = file_handling._valid_file(name=filename)
    if file_exists is True:
        temp = file_handling._read_file(filename, start, end)
        if temp is True:
            return render_template("output.html")
        else:
            return render_template("404.html", error=temp)
    else:
        return render_template("404.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
