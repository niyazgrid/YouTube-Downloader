from pytube import YouTube
from sys import argv
import os

link = argv[1]

try:
    yt = YouTube(link)
    print("Title:", yt.title)
    print("Views:", yt.views)

    # download in high resolution
    yd = yt.streams.get_highest_resolution()

    # set the folder path where you want to save the video
    download_folder = " "
    
    # check if the folder exists, if not create it
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # download the video to the specified folder
    yd.download(download_folder)
    
    print("Download successful!")
    
except Exception as e:
    print("An error occurred:", e)
