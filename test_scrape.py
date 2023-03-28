import unittest
import Scraper 

class TestScrape(unittest.TestCase):

    def test_scrape(self):
        self.assertAlmostEqual(Scraper.WriteToCSV(0))



if __name__== '__main__':
    unittest.main()