# YouTube Playlist Downloader and Title Renamer

This repository contains two Python scripts for downloading videos from a YouTube playlist and renaming them based on the titles from the playlist.

## Requirements

- Python 3.x
- `pytube` library

## Installation

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install pytube**: You can install the `pytube` library using pip. Open your terminal or command prompt and run:

   ```bash
   pip install pytube
   ```

## Usage

### Step 1: Download Videos from YouTube Playlist

1. **Run the Script**: Execute the first script to download the playlist:

   ```bash
   python youtube_playlist_downloader.py
   ```

2. **Get Titles**: This script will fetch the titles of the videos in the playlist and save them to a text file called `video_titles.txt`.

3. **Add to IDM**: Use Internet Download Manager (IDM) to import the `video_titles.txt` file as a batch. This will allow IDM to download all the videos in the playlist.

4. **Download Videos**: Start the download process in IDM. Ensure that the videos are saved in a new folder.

### Step 2: Fix Video Titles

1. **Run the Title Fixing Script**: After downloading, run the second script to rename the downloaded videos based on their titles:

   ```bash
   python fix_titles.py
   ```

2. **Input the Paths**: When prompted, provide:
   - The path to the YouTube playlist (for fetching titles).
   - The path to the folder where the videos were downloaded.

3. **Renaming**: The script will rename the downloaded videos according to the titles in the playlist.

## Example

- **YouTube Playlist URL**: `https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID`
- **Video Folder Path**: `C:\Users\Lokmane\Downloads\YourVideoFolder`

## Notes

- Ensure that the number of videos downloaded matches the number of titles fetched; otherwise, the renaming process may fail.
- If you encounter any issues, check if the paths provided are correct and if you have the necessary permissions.
