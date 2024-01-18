from pytube import Playlist

def download_playlist(url, folder_location, num_videos):
    try:
        # Create a Playlist object
        playlist = Playlist(url)

        # Get the videos in the playlist
        videos = playlist.videos

        # Limit the number of videos if specified
        if num_videos > 0:
            videos = videos[:num_videos]

        # Iterate through the videos and download them
        for video in videos:
            # Set the download location
            video.streams.first().download(folder_location)

        print("Download completed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get user input
    playlist_url = input("Enter the YouTube playlist URL: ")
    folder_location = input("Enter the folder location to save videos: ")
    num_videos = int(input("Enter the number of videos to download (Enter 0 for all): "))

    # Call the function to download the playlist
    download_playlist(playlist_url, folder_location, num_videos)
