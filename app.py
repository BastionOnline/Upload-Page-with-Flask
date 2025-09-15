from flask import Flask, request, send_file, render_template_string
import io
import threading
import webbrowser

app = Flask(__name__)

# HTML template for the upload page
upload_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Upload Text File</title>
</head>
<body>
    <h1>Upload a Text File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".txt" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file and uploaded_file.filename.endswith(".txt"):
            # Create a new text file in memory with "received"
            output = io.BytesIO()
            output.write(b"received")
            output.seek(0)
            return send_file(
                output,
                as_attachment=True,
                download_name="response.txt",
                mimetype="text/plain"
            )
        else:
            return "Please upload a valid .txt file.", 400
    return render_template_string(upload_html)

# Automatically open the browser when running
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(port=8000, debug=True)
