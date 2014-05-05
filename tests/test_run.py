import unittest
from IndicoIo.text.sentiment import political, spam, posneg

class FullAPIRun(unittest.TestCase):

    def test_political(self):
        political_set = set(['Libertarian', 'Liberal', 'Conservative', 'Green'])
        test_string = "Guns don't kill people, people kill people."
        response = political(test_string)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(political_set, set(response.keys()))

    def test_spam(self):
        spam_set = set(['Spam', 'Ham'])
        test_string = "Buy a new car!!"
        response = spam(test_string)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(spam_set, set(response.keys()))

    def test_posneg(self):
        posneg_set = set(['Positive', 'Negative'])
        test_string = "Worst song ever."
        response = posneg(test_string)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(posneg_set, set(response.keys()))

if __name__ == "__main__":
    unittest.main()
