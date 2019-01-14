import os
from pytube import YouTube
"""
    usage examples at https://github.com/NFicano/pytube
"""

SAVE_DIR = os.path.expanduser('~')

a = YouTube('https://www.youtube.com/watch?v=-----------')
print(a.streams.all())
stream = a.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download()
os.rename(stream.default_filename, SAVE_DIR + '/' + a.title + '.mp4')


#a = YouTube('https://www.youtube.com/watch?v=------------')
#for q in a.streams.filter(only_audio=True).all():
#    print(q)

#stream = a.streams.get_by_itag('171')
#stream.download()
#os.rename(stream.default_filename, SAVE_DIR + '/' + a.title + '.ogg')
