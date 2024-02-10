# Vetty Test

Python flask app to read text files queried by user.

Call to this route:

http://localhost:5000

for the application a read content of the default file(file1.txt) and render the results.

You can also give different file options (file1.txt, file2.txt, file3.txt OR file4.txt) and render properly it in HTML page.

After installing all dependencies, run the app by entering its folder and typing:

> $ flask --app app --debug run

This will run the flask app in debug mode.

Example route call to query file3:

http://localhost:5000/file3.txt

You can add query params with keys startline and endline, to only display content from '*startline*' to '*endline*'

http://localhost:5000/file3.txt?startline=5&endline=40
