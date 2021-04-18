# importing pytube and youtube
from pytube import YouTube

# audio download function
def download_audio(link):
    yt=YouTube(link)

    # video title
    print("Title of the video: ", yt.title)

    # artist/author name
    print("Author name: ", yt.author)

    # video rating
    print("Video rating: ", yt.rating)

    # video views
    print("Video views: ", yt.views)

    # getting audio file
    ys=yt.streams.filter(only_audio=True).all()
    
    # download to your system in prefered location
    print("Download started for Audio...")
    ys[0].download("./downloads/audio")
    print("Download finished!")

# video download function
def download_video(link):
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
    print("Download started for video...")
    ys.download("./downloads/video")
    print("Download finished!")

# accepting input from user
print("EG: https://www.youtube.com/watch?v=CDenUG1xMwg")
link = input("Enter YouTube video link: ")
print("You entered the link: ", link)

#User download choice
userChoice = input("Input *A* for Audio and *V* for Video: ")
print("Your selection: ", userChoice)

if userChoice == "v":
    download_video(link)
elif userChoice == "V":
    download_video(link)
elif userChoice == "a":
    download_audio(link)
elif userChoice == "A":
    download_audio(link)
else:
    print("Please enter *A* for Audio Download and *V* for Video Download")



