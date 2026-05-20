import time
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from uploader import upload_file

VIDEO_EXTENSIONS = ('.mp4' , '.mov' , '.avi' , '.mkv' , '.mxf' , '.prproj')

def is_file_stable(file_path, wait_seconds=10 , check_interval=5):
    """
    Waits Until the file size stop changing.
    This confirms the render is fully written to disk before we upload.

    Args:
        file_path         : Path to the file being checked
        wait_second       : How long the size must stay the same 
        check_interval    : How often (in seconds) to check the size
    """
    print (f"🫡 Goo bro you can leave , I can handle from here , Have fun , Your Butler Got you \n I will upload this : {os.path.basename(file_path)} after render ")

    stable_for = 0
    last_size = -1

    while stable_for < wait_seconds:
        try:
            current_size = os.path.getsize(file_path)
        except FileNotFoundError:
            return False
        
        if current_size == last_size:
            stable_for += check_interval
            print(f"  size stable for {stable_for}s / {wait_seconds}s... ")
        else:
            stable_for = 0
            print (f"   Still Writing... ({current_size / 1024 / 1024 :.1f} MB) ")
            

        last_size = current_size
        time.sleep(check_interval)
    
    print(f"😘 file is Stable Master , So I am getting Ready to upload it")
    return True


class VideoHandler (FileSystemEventHandler):
    """
    This class is called by watchdog whenever something happens in the folder.
    We only care about new video files being created;
    """
    
    def __init__ (self , folder_id):
        self.folder_id = folder_id

        self.processing = set()

    def on_created(self, event):
        if event.is_directory:
            return
        

        file_path = event.src_path
        _, ext =os.path.splitext(file_path)

        if ext.lower() not in VIDEO_EXTENSIONS:
            return
        

        if file_path in self.processing:
            return
        
        self.processing.add(file_path)
        print( f"\n Ok boss the video is detected : {os.path.basename(file_path)} ")

        if is_file_stable(file_path):
            try:
                upload_file(file_path, self.folder_id)
            except Exception as e:
                print(f"sry Master upload failed : {e} ")
            finally:
                self.processing.discard(file_path)

def start_watching(watch_folder, drive_folder_id):
    """
    Starts Watching the folder. Runs indefinitly until you press Ctrl+C.
    """

    event_handler = VideoHandler(drive_folder_id)
    observer = Observer()

    observer.schedule(event_handler, watch_folder, recursive=False)
    observer.start()


    print(f"\n Master my eyes 👁️ 👁️ are now open i am watch this folder : {watch_folder}")
    print(f" 📁 Uploading to Drive folder ID : {drive_folder_id}")


    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n Master Why did you cancled. ")

    observer.join()


