# importing pytube and youtube
from pytube import YouTube

# accepting input from user
link = input("Enter YouTube video link: ")
print("EG: https://www.youtube.com/watch?v=CDenUG1xMwg")
yt = YouTube(link)

# video title
print("Title of the video: ", yt.title)

# artist/author name
print("Author name: ", yt.author)

# video rating
print("Video rating: ", yt.rating)

# video views
print("Video views: ", yt.views)