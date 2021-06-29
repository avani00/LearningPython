'''get songs from song_names file
put songs into a list
sort list alphabetically using sorted()
move elements from list into seperate file for sorted songs'''

file_name = input('What song file do you want to sort? (Have in form "name of file".txt) ')

song_names = open(file_name)

song_names.seek(0)
songs = song_names.readlines()
songs.sort()
file_name = file_name.replace('.txt', '')
file_object  = open(f"{file_name}_sorted.txt", "w") 
for num in range(0,len(songs)):
	with open(f"{file_name}_sorted.txt", mode='a') as f:
		f.write(songs[num])