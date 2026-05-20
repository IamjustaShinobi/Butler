import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenaticate():
    """
    Handles Google login. On first run, opens browser for authorization.
    After that, reads saved token.json so no login needed again.
    """
    creds = None


    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open ('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def upload_file(file_path , folder_id):
    """
    Uploads a file to a specific Google Drive folder.

    Args :

          file_path : full path to the video file on your computer
          folder_id : The Google drive folder id brooo (after /folder/this part you better put your own brah)

    Returns :
          The Uploaded file ID on the Google drive
    """
    creds = authenaticate()

    service = build('drive' ,'v3' , credentials=creds )

    file_name = os.path.basename(file_path)

    file_metadata = {
        'name': file_name ,
        'parents' : [folder_id]
    }

    media = MediaFileUpload(
        file_path,
        mimetype='video/*',
        resumable=True
    )

    print(f"👆 ⬆️ 👆 Uploading bro , I got you GOOO Chill , I am your butler ")

    uploaded = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id, name'
    ).execute()

    print(f" 🫠 Its uploaded MASTER SHINOBI , Or koi render hai to btein malik ")
    return uploaded['id']
