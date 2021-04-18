# importing pytube and youtube
from pytube import YouTube

# accepting input from user
print("EG: https://www.youtube.com/watch?v=CDenUG1xMwg")
link = input("Enter YouTube video link: ")
print("You entered the link: ", link)
yt = YouTube(link)

# video title
print("Title of the video: ", yt.title)

# artist/author name
print("Author name: ", yt.author)

# video rating
print("Video rating: ", yt.rating)

# video views
print("Video views: ", yt.views)

# getting high resolution video stream
ys = yt.streams.get_highest_resolution()

# download to your system in prefered location
print("Download started ...")
ys.download("./downloads")
print("Download finished!")
