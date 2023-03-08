import unittest
import os

class TestIAOS(unittest.TestCase):
     #checks if the Bars image exists
     def test_bars_png_exists(self):
        self.assertTrue(os.path.exists('histogram_num_figures.jpg'))
     #checks if all the WordCloud exists
     def test_issue_3(self):
          for i in range(10):
               if not(os.path.exists('wordClouds/'+str(i+1)+'_WordCloud.png')):
                    assert False
          assert True

if __name__ == '__main__':
    unittest.main()