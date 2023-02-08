from pytube import YouTube
import os


def Download(link, data, name):
  youtubeObject = YouTube(link)
  
  if data == "video":
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
      out_file = youtubeObject.download()
      base, ext = os.path.splitext(out_file)
      new_file = name + ext
      os.chdir('D:/Dev/YoutubeDownloader/Downloads')
      os.rename(out_file, new_file)
    except:
      print("There has been an error in downloading your YouTube video!")
    print("Your download was successful!")


  elif data == "audio":
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    try:
      out_file = youtubeObject.download()

      base, ext = os.path.splitext(out_file)
      new_file = name + ".mp3"
      os.chdir('D:/Dev/YoutubeDownloader/Downloads')
      os.rename(out_file, new_file)
    except:
      print("There has been an error in downloading your YouTube audio!")
    print("Your download was successful!")

  else:
    print("Pleaser enter 'video' or 'audio'")



link = input("YouTube URL: ")
data = input("video/audio: ")
name = input("name: ")


Download(link, data, name)
