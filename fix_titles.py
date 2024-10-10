import os
import re

# Natural sorting helper function
def natural_key(text):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', text)]

# Folder containing the video files
video_folder = r"C:\Users\Lokmane\Downloads\aws course"

# Text file containing the list of titles
titles_file = r"C:\Users\Lokmane\Downloads\playlist_titles.txt"

# Get the list of video files, sorted naturally
video_files = sorted([f for f in os.listdir(video_folder) if f.startswith('videoplayback')], key=natural_key)

# Read the list of titles from the text file
with open(titles_file, 'r', encoding='utf-8') as f:
    titles = [line.strip() for line in f.readlines()]

# Ensure there are the same number of titles and video files
if len(video_files) != len(titles):
    print("Number of video files and titles do not match!")
else:
    # Loop through each video file and rename it using the corresponding title
    for i, video_file in enumerate(video_files):
        # Get the video file extension (e.g., .mp4, .mkv, etc.)
        file_extension = os.path.splitext(video_file)[1]
        
        # Construct the new file name using the corresponding title
        new_file_name = f"{titles[i]}{file_extension}"
        
        # Get the full path of the old and new file names
        old_file_path = os.path.join(video_folder, video_file)
        new_file_path = os.path.join(video_folder, new_file_name)
        
        # Rename the video file
        os.rename(old_file_path, new_file_path)
        
        print(f"Renamed '{video_file}' to '{new_file_name}'")

print("All videos have been renamed.")
