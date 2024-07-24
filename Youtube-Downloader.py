# downloading from youtube
import yt_dlp as youtube_dl

SAVE_PATH = 'C:/Users/ztben/Downloaded_Videos'

def Download(link):
    try:
        ydl_opts = {
            'outtmpl': f'{SAVE_PATH}/%(title)s.%(ext)s',
            'format': 'best'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        print(f'Error: {e}')


# ask for the link
inputLink = input("Enter the link here: \n>>> ")
Download(inputLink)
