import unittest

import numpy as np

from IndicoIo import political, spam, sentiment, fer, facial_features


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
        posneg_set = set(['Sentiment'])
        test_string = "Worst song ever."
        response = sentiment(test_string)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(posneg_set, set(response.keys()))

    def test_good_fer(self):
        fer_set = set(['Angry', 'Sad', 'Neutral', 'Surprise', 'Fear', 'Happy'])
        test_face = np.linspace(0,50,48*48).reshape(48,48).tolist()
        response = fer(test_face)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(fer_set, set(response.keys()))

    def test_bad_fer(self):
        fer_set = set(['Angry', 'Sad', 'Neutral', 'Surprise', 'Fear', 'Happy'])
        test_face = np.linspace(0,50,56*56).reshape(56,56).tolist()
        response = fer(test_face)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(fer_set, set(response.keys()))

    def test_good_facial_features(self):
        test_face = np.linspace(0,50,48*48).reshape(48,48).tolist()
        response = facial_features(test_face)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 48)


if __name__ == "__main__":
    unittest.main()
