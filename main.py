from watcher import start_watching

WATCH_FOLDER = r'PUT THE LOCATION OD THE FILE HERE'

DRIVE_FOLDER_ID = 'PUT THE FOLDER ID HERE'

if __name__ == '__main__':
    start_watching(WATCH_FOLDER, DRIVE_FOLDER_ID)