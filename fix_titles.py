import os
import re
from pytube import Playlist, exceptions

# Part 1: Fetch video titles from YouTube Playlist
# Replace with your playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Extract video titles
try:
    titles = [video.title for video in playlist.videos]
except exceptions.PytubeError as e:
    print(f"An error occurred while fetching titles: {e}")
    titles = []
# Check if titles were fetched successfully
if titles:
    print("Titles fetched successfully.")

    # Write titles to a text file (optional)
    titles_file = 'video_titles.txt'
    with open(titles_file, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')
    
    print("Titles saved to video_titles.txt")

    # Part 2: Rename video files based on titles
    # Folder containing the video files
    video_folder =  input("your saved vedios path: ") # Update with your path
    # Normalize the path (this will handle backslashes automatically)
    video_folder = os.path.normpath(video_folder)

    # Natural sorting helper function
    def natural_key(text):
        return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', text)]

    # Get the list of video files, sorted naturally (you can adjust the filter if needed)
    video_files = sorted([f for f in os.listdir(video_folder)], key=natural_key)

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
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{video_file}' to '{new_file_name}'")
            except OSError as e:
                print(f"Error renaming '{video_file}': {e}")

        print("All videos have been renamed.")
else:
    print("No titles fetched. Please check the playlist URL or try again.")
