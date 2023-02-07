from pytube import YouTube
import os


def Download(link, data):
  youtubeObject = YouTube(link)
  
  if data == "video":
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
      youtubeObject.download(output_path="./Downloads")
    except:
      print("There has been an error in downloading your YouTube video!")
    print("Your download was successful!")


  elif data == "audio":
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    try:
      out_file = youtubeObject.download(output_path="./Downloads")

      base, ext = os.path.splitext(out_file)
      new_file = base + ".mp3"
      os.rename(out_file, new_file)
    except:
      print("There has been an error in downloading your YouTube audio!")
    print("Your download was successful!")

  else:
    print("Pleaser enter 'video' or 'audio'")



link = input("YouTube URL: ")
data = input("video/audio: ")


Download(link, data)
