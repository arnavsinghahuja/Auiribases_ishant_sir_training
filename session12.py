
'''
1 resturnt have 1 menu
1 menu have lots of dishes

Amazon have many wender 
1 vender can have lots of product to sell

'''

"""
    1. Song: track, artists, album, duration
"""

class Song:

    def __init__(self, track, artists, album, duration):
        self.track = track
        self.artists = artists
        self.album = album
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Track:', self.track)
        print('Artists:', self.artists)
        print('Album:', self.album)
        print('Duration:', self.duration)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



song1 = Song(
                track='1. Laal Pari', 
                artists='john, jennie', 
                album='Album1', 
                duration=4.5
            )

song2 = Song(
                track='2. Zamaana Lage', 
                artists='harry, jennie', 
                album='Album1', 
                duration=3.5
            )

song3 = Song(
                track='3. Chor Bazaari', 
                artists='george, ben', 
                album='Album2', 
                duration=6.2
            )


# Linking of Objects with Each Other in next and previous form
# Hard Code
song1.next = song2
song2.next = song3
song3.next = song1

song1.previous = song3
song2.previous = song1
song3.previous = song2

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # 'e' was undefined; changed to 0

    # add is going to add a song in the linked list
    def add(self, song):
        print("Playlist (add) song:", song)
        if self.head is None:
            self.head = song
            self.tail = song
            self.size += 1
        else:
            # You can define a 'next' attribute on song to simulate linked list behavior
            self.tail.next = song
            song.previous = self.tail
            song.next = self.head
            self.head.previous = song
            self.tail = song

