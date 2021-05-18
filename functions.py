from pygame import mixer
from tinytag import TinyTag


def choose_song(num, song_list):
    num = int(num) - 1
    mixer.init()
    mixer.music.load(song_list[num])
    mixer.music.play()
    nowPlaying(song_list[num])
    return num


def choose_name(song_list):
    choose = int(input("\nWhich song to play? Choose its number: "))
    if 0 < choose <= len(song_list):
        track_no = choose_song(choose, song_list)
        return track_no
    else:
        choose_name(song_list)


def skip_song(num, song_list):
    num = num + 1
    if num < len(song_list) - 1:
        mixer.music.load(song_list[num])
        mixer.music.play()
    else:
        num = 0
        mixer.music.load(song_list[num])
        mixer.music.play()
    nowPlaying(song_list[num])
    return num


def prev_song(num, song_list):
    num = num - 1
    if num >= 0:
        mixer.music.load(song_list[num])
        mixer.music.play()
    else:
        num = len(song_list) - 2
        mixer.music.load(song_list[num])
        mixer.music.play()
    nowPlaying(song_list[num])
    return num


def nowPlaying(songName):
    tag = TinyTag.get(songName)
    try:
        print("Now Playing: " + tag.title + " by " + tag.artist)
    except tag.artist is None:
        print("Now Playing: " + tag.title)
