# 🤵 Butler — Auto Upload Renders to Google Drive

Never wait for a render to finish again.
Butler watches your export folder and automatically 
uploads your video to Google Drive the moment rendering is done.

## 📸 Demo
[screenshot of terminal]
[screenshot of drive]

## ✨ Who is this for
- Video Editors (Premiere Pro, DaVinci)
- 3D Designers (Blender, Cinema 4D, After Effects)
- Motion Artists
- Anyone who renders and has clients waiting

## ⚙️ How it works
1. You hit render in Premiere and walk away
2. Butler detects the new file in your export folder
3. Waits until render is 100% done (file size stable)
4. Auto uploads to your Google Drive client folder
5. You come back to an already uploaded file

## 🚀 Setup

### 1. Clone the repo
git clone https://github.com/yourname/Butler.git
cd Butler

### 2. Install dependencies
pip install -r requirements.txt

### 3. Google Cloud Setup
- Go to console.cloud.google.com
- Enable Google Drive API
- Create OAuth 2.0 credentials (Desktop app)
- Download as credentials.json and place in project root
- Add your Gmail as a test user in Audience settings

### 4. Configure main.py
WATCH_FOLDER = r'C:\Your\Render\Folder'
DRIVE_FOLDER_ID = 'your_drive_folder_id'

### 5. Run
python main.py

## 📦 Built With
- Python 3.13
- watchdog
- Google Drive API v3

## 🙋 Author
Your Name — linkedin.com/in/yourprofile