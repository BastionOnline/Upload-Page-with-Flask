from flask import Blueprint, render_template, request, send_file
import io

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]

        # Allow only .txt files
        if uploaded_file and uploaded_file.filename.endswith(".txt"):
            # Instead of saving or showing the content,
            # return a new text file to the user
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

    return render_template("upload.html")
