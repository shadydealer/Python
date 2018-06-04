from Utils.Song import Song

class Playlist:
    
    def __init__(self, *, name = None, repeat = False, shuffle = False):
        self.__songs = []
        self.__name = name
        self.__repeat = repeat
        self.__shuffle = shuffle

    def add_song(self,song):
        if type(song) is not Song:
            raise TypeError(f'Argument must be of type {type(Song)}.\n')
        self.__songs.append(song)

    def remove_song(self, song):
        if type(song) is not Song:
            raise TypeError(f'Argument must of type {type(Song)}.\n')
        if song not in self.__songs:
            print(f'Song: {song} is not in the playlist.\n')
        else:
            self.__songs.remove(song)
    
    def add_songs(self, song):
        
        if type(songs) is not list:
            raise TypeError(f'Argument must be of type {type(list)} of {type(Song)}.\n')
        
        for song in songs:
            if type(song) is not Song:
                raise TypeError(f'List object must be of type {type(Song)}.\n')

        for song in songs:
            self.add_song(song)

    def total_length(self):
        result = 0
        for song in self.__songs:
            result += song.length(seconds = True)
        
        seconds = result % 60
        minutes = result//60
        hours = minutes //60
        minutes %= 60

        return f'{hours}:{minutes}:{seconds}'
