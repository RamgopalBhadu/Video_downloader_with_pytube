from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=wF_B_aagLfI")
dw = yt.streams.get_by_itag(140)
dw.download("D:/")
