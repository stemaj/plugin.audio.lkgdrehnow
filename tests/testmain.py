import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from resources.lib import main
from resources.lib import read

class Test_1(unittest.TestCase):

  def test_1(self):
    data = read.load_file('000')
    arr = main.listOfNewest(data)
    self.assertEqual(10, len(arr))
    self.assertEqual('http://lkg-drehnow.de/wordpress/wp-content/uploads/2019/03/190317_Matthias-Mempel_Jesus-und-Nikodemus_Johannes314-21.mp3', arr[9].link)
    self.assertEqual(' (Joh. 3, 14-21) &#8211; 17.03.2019 &#8211; Matthias Mempel', arr[9].film)
    self.assertEqual('Jesus und Nikodemus', arr[9].plot)
