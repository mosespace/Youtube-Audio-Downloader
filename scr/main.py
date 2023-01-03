from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
  try:
      youtubeObject.Download()
  except:
    print("There has been an error in downloading your youtube video, check your internet connection and try again")
  else:
    print("This download has completed! Follow me on github @mosespace")

link = input("Put your youtube link here!! URL: ")
Download(link)