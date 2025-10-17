import os, time
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

app = Flask(__name__)
SAVE_DIR = "diary_entries"
os.makedirs(SAVE_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp3", "mp4", "wav", "txt", "pdf"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def diary():
    if request.method == "POST":
        entry_text = request.form.get("entry", "").strip()
        if entry_text:
            fname = f"entry_{time.strftime('%Y%m%d_%H%M%S')}.txt"
            with open(os.path.join(SAVE_DIR, fname), "w", encoding="utf-8") as f:
                f.write(entry_text)

        if "file" in request.files:
            file = request.files["file"]
            if file and allowed_file(file.filename):
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                safe_name = f"{timestamp}_{file.filename}"
                file.save(os.path.join(SAVE_DIR, safe_name))

        return redirect(url_for("diary"))

    files = os.listdir(SAVE_DIR)
    files.sort(reverse=True)  # newest first

    return render_template_string("""
        <h2>My Diary</h2>
        <form method="post" enctype="multipart/form-data">
            <label>Diary entry:</label><br>
            <textarea name="entry" rows="5" cols="40"></textarea><br><br>

            <label>Upload file:</label><br>
            <input type="file" name="file"><br><br>

            <button type="submit">Save</button>
        </form>

        <h3>Saved Entries & Files</h3>
        <ul>
        {% for f in files %}
            <li>
                <a href="{{ url_for('download_file', filename=f) }}" target="_blank">{{ f }}</a>
            </li>
        {% endfor %}
        </ul>
    """, files=files)

@app.route("/files/<path:filename>")
def download_file(filename):
    return send_from_directory(SAVE_DIR, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(debug=True)

