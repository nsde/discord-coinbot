from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

for stream in str(yt.streams).split('<Stream:'):
    print(stream)