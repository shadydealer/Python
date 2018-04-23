import unittest 

from Utils.Song import Song
from Utils.Playlist import Playlist

class TestSongClass(unittest.TestCase):
    def setUp(self):
            self.s = Song(title="Odin",
                    artist="Manowar",
                    album="The Sons of Odin",
                    length="3:44")

    def test_song_instance_creation(self):
        with self.subTest("Test if validate_minutes_or_seconds throws Value Error"):
            with self.assertRaises(ValueError):
                Song.validate_minutes_or_seconds(60)
        
        with self.subTest("Test if validate_hours throws Value Error"):
            with self.assertRaises(ValueError):
                Song.validate_hours(-1)

        def test_valid_length(self):
            
            self.assertTrue(hasattr(self.s, "title")  and
                            hasattr(self.s,"artist")  and
                            hasattr(self.s,"album")   and
                            hasattr(self.s,"length"))
    
    def test_song_instance__str_(self):
        valid_output = 'Manowar - Odin from The Sons of Odin - 3:44.'
        self.assertEqual(str(self.s),
                        valid_output)
    
    def test_song_hash(self):
        self.assertEqual(hash(self.s), hash(str(self.s)))
    
    def test_song_eq(self):
        temp = Song(title="Odin",
                    artist="Manowar",
                    album="The Sons of Odin",
                    length="3:44")

    def test_length_method(self):
        temp = Song(title="Odin",
                    artist="Manowar",
                    album="The Sons of Odin",
                    length="3:44:30")

        with self.subTest('Raises Value error uppon getting more than 1 argument.'):
            with self.assertRaises(ValueError):
                temp.length(seconds = True, minutes = True)

        with self.subTest('Raises Value error uppon getting an invalid keyword.'):
            with self.assertRaises(ValueError):
                temp.length(invalid = True)

        with self.subTest('Returns lengths str representation if no parameters were passed.'):
            self.assertEqual(temp.length(), "3:44:30")

        with self.subTest('Test length method with seconds as parameter.'):
          self.assertEqual(temp.length(seconds = True),3*(60**2)+44*60+30)

        with self.subTest('Test length method with minutes as paramter.'):
            self.assertEqual(temp.length(minutes = True), 3*60 + 44)

        with self.subTest('Test length method with hours as parameter.'):
            self.assertEqual(temp.length(hours = True), 3)

class TestPlaylistClass(unittest.TestCase):
    def setUp(self):
        self.p = Playlist(name = 'Works')
        self.s = Song(title="Odin",
                artist="Manowar",
                album="The Sons of Odin",
                length="3:44:30")

        for i in range(0,2):
            self.p.add_song(self.s)
    
    def test_total_length(self):
        self.assertEqual(self.p.total_length(), '7:29:0')

if __name__ == '__main__':
    unittest.main()
