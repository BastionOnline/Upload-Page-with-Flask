from flask import Flask, request, send_file, render_template
import io
from int import generate_random_int

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('upload.html')


@app.route("/", methods=["POST"])
def recieved():
    uploaded_file = request.files.get("file")
    if uploaded_file and uploaded_file.filename.endswith(".txt"):
        
        randomNumber = generate_random_int()
        
        # Create a new text file in memory with "received"
        output = io.BytesIO()
        output.write(str(randomNumber).encode('utf-8'))
        output.seek(0)
        return send_file(
            output,
            as_attachment=True,
            download_name="response.txt",
            mimetype="text/plain"
        )
    else:
        return "Please upload a valid .txt file.", 400


if __name__ == "__main__":
    app.run(port=8001, debug=False)