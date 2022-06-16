from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import time
import json
import os, sys




class Handler(FileSystemEventHandler):
    
    def on_modified(self, event):
        for file in os.listdir(watched_folder):
            src = f"{watched_folder}/{file}"
            dst = f"{destination_folder}/{file}"
            os.rename(src=src,dst=dst)


if __name__ == "__main__":
    watched_folder = input("Watched folder path:")
    destination_folder = input("Destination folder path:")
    handler = Handler()
    observer = Observer()
    observer.schedule(event_handler=handler, path=watched_folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
