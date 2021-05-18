from pygame import mixer
import file_names as fn
from tinytag import TinyTag
import functions

fn.create_music_names()

with open("file_names.txt") as file:
    songs = file.read()
    song_list = songs.split("\n")
print("\nSongs available to play:")
for i in range(len(song_list) - 1):
    tag = TinyTag.get(song_list[i])
    print(str(i + 1) + ". " + tag.title)

check = "Start"
number = functions.choose_name(song_list)

i = 0
while i < 1:

    check = input("\nWhat to do? Type QUIT to quit: ")
    check = check.upper()

    if check == "PAUSE" or check == "||":
        mixer.music.pause()
        print("Music paused")

    elif check == "RESUME" or check == ">|":
        mixer.music.unpause()
        print("Music resumed")

    elif check == "CHANGE":
        number = functions.choose_name(song_list)

    elif check == "SKIP" or check == ">>":
        number = functions.skip_song(number, song_list)

    elif check == "REWIND" or check == "<":
        mixer.music.rewind()
        print("Now Playing:" + song_list[number])

    elif check == "PREV" or check == "<<":
        number = functions.prev_song(number, song_list)

    elif check == "QUIT":
        mixer.music.stop()
        i = 1

    else:
        print("Invalid Input.Please try again.")
