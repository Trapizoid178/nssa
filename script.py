#!/usr/bin/env python3

import subprocess
import datetime
import os

# -------------------------------
# Configuration
# -------------------------------
SOURCE = "/www/virtualhosts/"
DEST = "/backups/virtualhosts/"
LOGFILE = "/var/log/python-backup.log"

# Make sure backup destination exists
os.makedirs(DEST, exist_ok=True)

def log(message):
    """Write timestamped messages to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGFILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def run_backup():
    log("Backup started.")

    # rsync command
    rsync_cmd = [
        "rsync",
        "-av",
        "--delete",
        SOURCE,
        DEST
    ]

    try:
        result = subprocess.run(rsync_cmd, capture_output=True, text=True)

        # Log rsync output
        if result.stdout:
            log("RSYNC OUTPUT:")
            log(result.stdout)

        # Handle errors
        if result.stderr:
            log("RSYNC ERRORS:")
            log(result.stderr)

        if result.returncode == 0:
            log("Backup completed successfully.")
        else:
            log(f"Backup failed with return code {result.returncode}")

    except Exception as e:
        log(f"Exception occurred: {str(e)}")

    log("-------------------------------")

if __name__ == "__main__":
    run_backup()