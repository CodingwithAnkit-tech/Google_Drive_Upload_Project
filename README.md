# 🚀 Google Drive Upload Project (Flask + OAuth + Render Deployment)

A production-ready Flask web application that allows users to upload files directly to Google Drive using Google OAuth 2.0 authentication.

🔗 Live App: https://google-drive-upload-project.onrender.com

---

## 📌 Project Overview

This project demonstrates:

- Google OAuth 2.0 Authentication
- Google Drive API integration
- File upload handling in Flask
- Secure environment variable management
- Production deployment on Render
- GitHub integration

Users authenticate with Google and upload files to a specific Google Drive folder.

---

## 🛠 Tech Stack

- Python 3
- Flask
- Google Drive API
- Google OAuth 2.0
- Gunicorn
- Render (Deployment)
- GitHub

---

## 🔐 Features

- Google Login Authentication
- Secure Token Storage
- Upload File to Specific Drive Folder
- Frontend UI (HTML + CSS)
- Production Deployment Support
- Environment Variable Based Credential Management

---

## 📂 Project Structure

Google_Drive_Upload_Project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── templates/
└── index.html


---

## ⚙️ Setup Instructions (Local Development)

 1️⃣ Clone the Repository

```bash
git clone https://github.com/CodingwithAnkit-tech/Google_Drive_Upload_Project.git
cd Google_Drive_Upload_Project

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Google Cloud Project

= Go to Google Cloud Console
- Create New Project
- Enable Google Drive API
- Create OAuth 2.0 Credentials
- Add Redirect URIs:

# For Local :

http://localhost:5000/oauth2callback

# For Production:

https://google-drive-upload-project.onrender.com/oauth2callback

- Download credentials.json for local use.

5️⃣ Run Application
python app.py

Open:

http://localhost:5000

Authenticate at:

http://localhost:5000/auth

### 🌍 Production Deployment (Render)
Step 1: Push Code to GitHub
- Make sure:
- credentials.json is NOT uploaded
- .gitignore excludes secrets

Step 2: Create Web Service on Render

- Select GitHub repo
- Runtime: Python 3
- Build Command:
- pip install -r requirements.txt
- Start Command:
- gunicorn app:app

Step 3: Add Environment Variable in Render

- Add:
- Key:
- GOOGLE_CREDENTIALS
- Value:
- Paste entire credentials.json content (single line JSON)

Step 4: Deploy

- After deployment, open:

---     https://google-drive-upload-project.onrender.com/auth
- Authenticate and start uploading.

# 🔄 Application Flow

- User clicks Upload
- If not authenticated → Redirect to /auth
- Google OAuth login
- Google redirects to /oauth2callback
- Token saved
- File uploaded to Google Drive
- Direct download link returned

# 📊 What This Project Demonstrates

- API Integration
- OAuth 2.0 Flow
- Secure Secret Handling
-Backend + Frontend Integration
- Production Deployment
- Cloud Hosting
- Real-world authentication system

# 🚀 Future Improvements

- Multi-user token storage (Database)
- File listing feature
- File delete option
- Progress bar UI
- User-specific Drive folder creation

👨‍💻 Author

Ankit Verma
B.Tech CSE | Python Data Analyst | Python Developer

⭐ If You Like This Project

-  Give it a star ⭐ on GitHub!









