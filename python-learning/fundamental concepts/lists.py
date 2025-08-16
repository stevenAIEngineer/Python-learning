songs = ["Matilda", "Sweet Creatue", "If I Could Fly", "Right Now"]

for song in songs:
    print("Love listening to ", song)
    
songs.append("Story Of My Life")
songs.remove("Right Now")

print("Updated playlists: ", songs)