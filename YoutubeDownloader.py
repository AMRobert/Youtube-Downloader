import pytube
link="https://youtu.be/oz6yHtNMFhc"; #Link of the Youtube Video
yt = pytube.YouTube(link)
stream=yt.streams.get_highest_resolution() #Resolution of video
stream.download('F:\AMR') #Stoarge Path
