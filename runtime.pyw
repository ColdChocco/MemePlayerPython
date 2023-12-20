import os
import random
import time
import winsound

# Get a list of all files in the current directory
files = os.listdir(os.getcwd())

# Filter out non-mp3 files
songs = [file for file in files if file.endswith('.wav')]

while True:
	# Choose a random song
	song_to_play = random.choice(songs)
	
	# Use the OS command to play the song
	winsound.PlaySound(song_to_play, winsound.SND_ASYNC)
	
	time.sleep(random.randint(60, 500))
