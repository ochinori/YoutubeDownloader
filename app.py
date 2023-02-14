from pytube import YouTube
import os
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("YouTube Downloader")
        self.geometry("700x220+1000+500")
        self.resizable(height=False, width=False)
        self.iconbitmap("D:\Dev\YoutubeDownloader\Youtube.ico")


        # configure grid layout
        self.grid_columnconfigure(2, weight=1)


        # label
        self.logo_label = customtkinter.CTkLabel(self, text="YouTube Downloader", font=customtkinter.CTkFont(size=20, weight="bold"), width=700)
        self.logo_label.grid(row=0, column=0, columnspan=3, padx=5, pady=(5, 5))

        # Entry
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=1, column=0, columnspan=3, padx=(5, 5), pady=(7, 5), sticky="nsew")

        self.entry_frame.grid_columnconfigure(1, weight=1)
        self.entry_frame.grid_columnconfigure((0,2), weight=0)



        # URL label
        self.url_label = customtkinter.CTkLabel(self.entry_frame, text="URL:", font=customtkinter.CTkFont(size=16), width=20)
        self.url_label.grid(row=0, column=0, padx=(7, 5), pady=(7, 5))

        # URL entry
        self.url_entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="https://www.youtube.com/watch...")
        self.url_entry.grid(row=0, column=1, columnspan=2, padx=(5, 10), pady=(5, 0), sticky="nsew")


        # name
        self.name_entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Name", height=35)
        self.name_entry.grid(row=1, column=0, columnspan=2, padx=(5, 0), pady=(7, 0), sticky="nsew")

        # type
        self.datatype = customtkinter.CTkOptionMenu(master=self.entry_frame, dynamic_resizing=False, width=80, values=[".mp4", ".mp3"])
        self.datatype.grid(row=1, column=2, padx=10, pady=(7, 0))

        # buttons
        self.download_button = customtkinter.CTkButton(self, width=500, height=35, text="Download", command=self.download)
        self.download_button.grid(row=2, column=0, columnspan=2, padx=(7, 5), pady=(7, 5), sticky="ew")

        self.open_folder = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), height=35, text="Open Folder", command=self.openFolder)
        self.open_folder.grid(row=2, column=2, padx=(5, 5), pady=(7, 5), sticky="ew")


        self.process_label = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=16))
        self.process_label.grid(row=3, column=0, padx=(8, 5), pady=(7, 5), sticky="w")

    # download function
    def download(self):

      # download process (doesn't work)
      self.process_label.configure(text="downloading...")


      # getting inputs
      datatype = self.datatype.get()
      name = self.name_entry.get()

      # creates download folder if it doesn't exists and changes directory
      if os.path.exists('C:/Users/Kevin/Desktop/YTDownloads') == True and os.path.isdir('C:/Users/Kevin/Desktop/YTDownloads'):
        os.chdir('C:/Users/Kevin/Desktop/YTDownloads')
      else:
        os.mkdir('C:/Users/Kevin/Desktop/YTDownloads')
        os.chdir('C:/Users/Kevin/Desktop/YTDownloads')

     

      # video download
      if datatype == ".mp4":
        
        try:
      
          youtubeObject = YouTube(self.url_entry.get())
          youtubeObject = youtubeObject.streams.get_highest_resolution()
                  
          out_file = youtubeObject.download()
          
          base, ext = os.path.splitext(out_file)
          new_file = name + ext
          os.rename(out_file, new_file)

          self.process_label.configure(text="Download was successful!")

        except:

          self.process_label.configure(text="There was an error in downloading your video!")
        

      # audio download
      else: 
        try:
          
          youtubeObject = YouTube(self.url_entry.get())
          youtubeObject = youtubeObject.streams.filter(only_audio=True).first()

          out_file = youtubeObject.download()
          
          base, ext = os.path.splitext(out_file)
          new_file = name + ".mp3"
          os.rename(out_file, new_file)

          self.process_label.configure(text="Download was successful!")

        except:

          self.process_label.configure(text="There was an error in downloading your audio!")
        
      # clearing entrys and changing focus to name
      self.url_entry.delete(first_index=0, last_index='end')
      self.name_entry.delete(first_index=0, last_index='end')
      self.url_entry.focus()



    # open download folder
    def openFolder(self):
      os.startfile('C:/Users/Kevin/Desktop/YTDownloads')


# running app
if __name__ == "__main__":
    app = App()
    app.mainloop()
