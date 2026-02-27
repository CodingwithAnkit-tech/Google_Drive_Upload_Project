import json
from flask import Flask, request, jsonify, redirect, render_template
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from werkzeug.utils import secure_filename
import os
import pickle
import mimetypes
import tempfile

# 🔥 Allow HTTP for localhost only
#os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
CORS(app)

# =========================
# 🔐 CONFIG
# =========================
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
FOLDER_ID = "1R018uxA7eUmjvvK5YILzXXuy4SV5I-PY"   # ✅ Your Folder ID
app.secret_key = "supersecretkey"


# =========================
# 🔑 AUTH ROUTE
# =========================
@app.route("/auth")
def auth():
    if os.environ.get("GOOGLE_CREDENTIALS"):
        creds_json = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        flow = Flow.from_client_config(
            creds_json,
            scopes=SCOPES,
            redirect_uri=request.host_url + "oauth2callback"
        )
    else:
        flow = Flow.from_client_secrets_file(
            "credentials.json",
            scopes=SCOPES,
            redirect_uri=request.host_url + "oauth2callback"
        )

    auth_url, _ = flow.authorization_url(prompt="consent")
    return redirect(auth_url)


# =========================
# 🔁 OAUTH CALLBACK
# =========================
@app.route("/oauth2callback")
def oauth2callback():
    if os.environ.get("GOOGLE_CREDENTIALS"):
        creds_json = json.loads(os.environ["GOOGLE_CREDENTIALS"])
        flow = Flow.from_client_config(
            creds_json,
            scopes=SCOPES,
            redirect_uri=request.host_url + "oauth2callback"
        )
    else:
        flow = Flow.from_client_secrets_file(
            "credentials.json",
            scopes=SCOPES,
            redirect_uri=request.host_url + "oauth2callback"
        )

    flow.fetch_token(authorization_response=request.url)

    with open("token.pickle", "wb") as token:
        pickle.dump(flow.credentials, token)

    return redirect("/")


# =========================
# 📤 UPLOAD ROUTE (FINAL FIXED)
# =========================
@app.route("/upload", methods=["POST"])
def upload():
    if not os.path.exists("token.pickle"):
        return jsonify({"error": "Authenticate first at /auth"}), 401

    if "file" not in request.files:
        return jsonify({"error": "No file selected"}), 400

    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)

    # Save temp file
    temp_path = os.path.join(os.getcwd(), filename)
    uploaded_file.save(temp_path)

    mime_type, _ = mimetypes.guess_type(temp_path)
    if not mime_type:
        mime_type = "application/octet-stream"

    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": filename,
        "parents": [FOLDER_ID]
    }

    media = MediaFileUpload(temp_path, mimetype=mime_type)

    uploaded = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    # 🔥 IMPORTANT: Explicitly close media
    media.stream().close()

    # Safe remove
    try:
        os.remove(temp_path)
    except Exception as e:
        print("Temp file delete skipped:", e)

    file_id = uploaded.get("id")
    file_link = f"https://drive.google.com/uc?id={file_id}"

    return jsonify({
        "message": "File uploaded successfully",
        "link": file_link
    })


# =========================
# 🏠 HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)
