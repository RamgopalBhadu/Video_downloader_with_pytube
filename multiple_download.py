from pytube import YouTube
video_list = open("sample.txt",'r')

for i in video_list:
    yt = YouTube(i)
    dw =yt.streams.first()
    dw.download("D:/")
    
