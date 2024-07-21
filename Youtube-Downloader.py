# pytube practice downloading from youtube
# from pytube import YouTube
import yt_dlp as youtube_dl

SAVE_PATH = 'C:/Users/ztben/Downloaded_Videos'

# def Download(link):
#     try:
#         yt = YouTube(link)
#         print(f'Title: {yt.title}')
#         print(f'Author: {yt.author}')
#         print(f'Length: {yt.length} seconds')

#         # highResVid = yt.streams.filter(file_extension='mp4').get_highest_resolution()
#         # streams = yt.streams.all()
#         # for stream in streams:
#         #     print(stream)
#         print(yt.check_availability())
    
#         vid = yt.streams.first()
#         print(f'Selected Stream: {vid}')
    
#         vid.download(output_path=SAVE_PATH)
#         print('Download Complete!')
#     except Exception as e:
#         print(f'Error: {e}')

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
