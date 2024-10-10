from pytube import Playlist

# Replace with your playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLdXLsjL7A9k3L9zf0Cy7j_cV6sx9lXeZO"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Extract video titles
titles = [video.title for video in playlist.videos]

# Write titles to a text file
with open('video_titles.txt', 'w') as f:
    for title in titles:
        f.write(title + '\n')

print("Titles saved to video_titles.txt")
