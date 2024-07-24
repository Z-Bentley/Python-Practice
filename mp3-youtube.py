# downloading mp3 files from YouTube
import yt_dlp
import os

SAVE_PATH = 'C:/Users/ztben/Downloaded_Videos'

# def downloadAudio(link):
#     with yt_dlp.YoutubeDL({'extract_audio': True, 
#                            'format': 'bestaudio', 
#                            'outtmpl': f'{SAVE_PATH}/%(title)s.mp3'
#                            }) as video:
#         infoDict = video.extract_info(link, download = True)
#         videoTitle = infoDict['title']
#         print(videoTitle)

def downloadPlaylist(link):
    try:
        ydl_opts = {
            'outtmpl': f'{SAVE_PATH}/%(playlist)s/%(title)s.mp3',
            'format': 'bestaudio',
            'noplaylist': False,
            'verbose': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print('Playlist download complete')
    except Exception as e:
        print(f'error: {e}')

# inputLink = 'https://www.youtube.com/playlist?list=PLHvbCLw20EPr5UgtDdh_6SouEdWP11vDg'
inputLink = input("Enter the link here: \n>>> ")
downloadPlaylist(inputLink)
