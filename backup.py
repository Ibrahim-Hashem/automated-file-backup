import os 
import shutil
import datetime
import schedule
import time

source_dir = '' # Path to the folder you want to backup
destination_dir = '' # Path to the directory where you want to store the backup

def copy_folfer_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest_dir}")

def backup():
    copy_folfer_to_directory(source_dir, destination_dir)

schedule.every().day.at("00:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)
