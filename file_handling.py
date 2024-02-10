import re
import codecs


class FILE_HANDLING(object):
    def __init__(self) -> None:
        self.files = ["file1", "file2", "file3", "file4"]

    # creating output html file to render to front-end and preserve markup(if-any)
    def _read_file(self, filename, start, end):
        try:
            startline = 0
            endline = 0
            f = codecs.open(
                r"data/" + filename, "r+", encoding="utf-8", errors="ignore"
            )
            f1 = open(r"templates/output.html", "w")
            f1.write(r'{% extends "index.html" %}')
            f1.write(r"{% block content %}")
            total_lines = f.readlines()
            length = len(total_lines)
            if (
                start >= 0
                and start < length
                and end >= 0
                and end < length
                and end > start
            ):
                startline = start
                endline = end - 1
            else:
                endline = length - 1
            for i, x in enumerate(total_lines):
                if i >= startline:
                    f1.write(x)
                    f1.write("<br>")
                    if i > endline:
                        break
            f1.write(r"{% endblock %}")
            f.close()
            f1.close()
            return True
        except Exception:
            return str(Exception)

    # checking if the filename provided adheres to the application requirements
    def _valid_file(self, name) -> bool:
        file_name = re.split(r"\s", name)
        for file in self.files:
            if re.search(file, file_name[0]):
                return True
        return False
