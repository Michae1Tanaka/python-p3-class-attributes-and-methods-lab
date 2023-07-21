class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, song_name, song_artist, song_genre):
        self.name = song_name
        self.artist = song_artist
        self.genre = song_genre
        self.add_song_to_count()
        self.add_to_genres(song_genre)
        self.add_to_artists(song_artist)
        self.add_to_genre_count(song_genre)
        self.add_to_artist_count(song_artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song_genre):
        cls.genres.append(song_genre)

    @classmethod
    def add_to_artists(cls, song_artist):
        cls.artists.append(song_artist)

    @classmethod
    def add_to_genre_count(cls, song_genre):
        # for genre in cls.genre_count:
        if song_genre in cls.genre_count:
            cls.genre_count[song_genre] += 1
        else:
            cls.genre_count[song_genre] = 1

    @classmethod
    def add_to_artist_count(cls, song_artist):
        if song_artist in cls.artist_count:
            cls.artist_count[song_artist] += 1
        else:
            cls.artist_count[song_artist] = 1
