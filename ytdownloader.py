from pytube import YouTube

def download(link):
    youtubeObject= YouTube(link)
    youtubeObject= youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has ocurred.")
    print("The download is complete.") 

link=input("Enter url to the video you want to download:")
download(link)           