from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("There has been an error in downloading yout YouTube video!")
  print("Your download was successful!")


  link = input("YouTube URL: ")
  Download(link)