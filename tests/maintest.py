import unittest
from resources.lib import read
from resources.lib import main

class Test_ParseFiles(unittest.TestCase):

    def test_file000(self):
        a = read.load_file('000')
        b = main.getAllFilms(a)
        self.assertEqual(23, len(b))
        c = main.getAllThema(a)
        self.assertEqual(23, len(c))
        d = main.getAllMp3(a)
        self.assertEqual(23, len(d))

