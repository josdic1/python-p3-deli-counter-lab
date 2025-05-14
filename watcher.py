from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

WATCH_FILE = "lib/deli_counter.py"

class RunOnSaveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(WATCH_FILE):
            os.system("clear")
            print("🔁 Change detected — running script...")
            subprocess.run(["python3", WATCH_FILE])

observer = Observer()
observer.schedule(RunOnSaveHandler(), path="lib", recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()