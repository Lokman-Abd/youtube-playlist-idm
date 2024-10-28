from pytube import Playlist  
 
def get_video_links_from_playlist(playlist_url): 
    playlist = Playlist(playlist_url) 
    return [video.watch_url for video in playlist.videos]  
 
def write_to_file_and_display(video_urls, file_name='youtube_video_links.txt'): 
    with open(file_name, 'w') as file: 
        for url in video_urls: 
            print(url) 
            file.write(url + '\n')  
 
# Replace with your playlist URL 
playlist_url = 'https://www.youtube.com/watch?v=31ieHmcTUOk&list=PL4cUxeGkcC9hxjeEtdHFNYMtCpjNBm3h7' 
video_urls = get_video_links_from_playlist(playlist_url) 
write_to_file_and_display(video_urls)  