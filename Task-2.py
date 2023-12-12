import os
import shutil
import time
import time as datetime

#checking if file has been created or modified in the last 24 hours
def is_recent_file(file):
    file_stats = os.stat(file)
    """ there might be error with windows
    file_path = 'C:/Users/imrey/NTUSER.DAT'
    
    try:
        # Skip system files
        if os.path.basename(file_path).startswith('NTUSER'):
            return False
        
    except PermissionError as e:
        print(f"PermissionError: {e}. Skipping file: {file_path}")
        return False """
    # Get the modification time and creation time in seconds
    mod_time = file_stats.st_mtime
    creation_time = file_stats.st_ctime
    # Calculate the d/nce in seconds
    time_difference = time.time() - max(mod_time, creation_time)
    # If the time d/nce is less than 24 hours which is 86400 seconds.. take the file as recent
    return time_difference < 86400

# Function to update the identified files
def update_files(files):
    for file in files:
        with open(file, 'a') as f:
            f.write("\nUpdated at " + time.ctime())

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Identify files created or modified in the last 24 hours
recent_files = [f for f in files if is_recent_file(f)]

# Check if "last_24hours" folder exists, if not create it
if not os.path.exists("last_24hours"):
    os.mkdir("last_24hours")
    

# Update the identified files
update_files(recent_files)

# Move the updated files to the "last_24hours" folder
if recent_files:
    #printing all files in the directory 
    print(f"All files in the directory {os.listdir()}") # or print(files)
    #update_files(recent_files)
    print("Recent files identified:", recent_files)
    for file in recent_files:
        shutil.move(file, os.path.join("last_24hours", file))
        
    print(f"The file {files} have been updated and moved to 'last_24hours' folder.")
else:
    print ("No recent file identified. All recent files have been updated and moved to the 'last_24hours' folder. ")
