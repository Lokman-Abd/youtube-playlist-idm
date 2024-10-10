import os
from pytube import Playlist, YouTube
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to extract video URLs from the playlist
def get_playlist_video_urls(playlist_url):
    playlist = Playlist(playlist_url)
    return [video_url for video_url in playlist.video_urls]

# Function to get the video title using PyTube
def get_video_title(video_url):
    try:
        # Use PyTube to get the video title
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Error fetching title for {video_url}: {e}")
        return None

# Function to get the direct download link using yt-dlp
def get_direct_download_link(video_url):
    try:
        # Use yt-dlp to get the direct download link for the best video quality
        result = subprocess.run(
            ['yt-dlp', '-f', 'best', '-g', video_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error fetching direct link for {video_url}: {e}")
        return None

# Function to create IDM batch download file with correct video titles
def create_idm_batch_file(playlist_url, output_file="idm_batch_download.txt", max_workers=8):
    video_urls = get_playlist_video_urls(playlist_url)
    
    # Use ThreadPoolExecutor to parallelize fetching of titles and direct download links
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks to fetch video titles and links concurrently
        future_to_url_title = {executor.submit(get_video_title, url): url for url in video_urls}
        future_to_url_link = {executor.submit(get_direct_download_link, url): url for url in video_urls}
        
        with open(output_file, 'w') as f:
            # Process futures as they complete, fetching titles and links
            for future_title, future_link in zip(as_completed(future_to_url_title), as_completed(future_to_url_link)):
                video_url_title = future_to_url_title[future_title]
                video_url_link = future_to_url_link[future_link]
                
                try:
                    title = future_title.result()
                    direct_link = future_link.result()

                    if title and direct_link:
                        # Remove any illegal characters from the title for file naming
                        safe_title = "".join(c if c.isalnum() or c in " .-_()" else "_" for c in title)
                        # Write to the batch file: URL + output file name
                        f.write(direct_link + '\n')
                        f.write(f"out={safe_title}.mp4\n")
                    else:
                        print(f"Skipping {video_url_title} due to missing data.")
                except Exception as e:
                    print(f"Error processing video {video_url_title}: {e}")
    
    print(f"IDM batch file created: {output_file}")

if __name__ == "__main__":
    # Example: YouTube Playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")
    
    # Generate IDM batch download file with parallel processing
    create_idm_batch_file(playlist_url)
