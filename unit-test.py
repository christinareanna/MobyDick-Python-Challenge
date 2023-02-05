import unittest
from cleanwords import getStopWordsSet, get_top_words

# Test to get stop words

class TestGetStopWordsSet(unittest.TestCase):
    def test_get_stop_words_set(self):
        stop_words_text = ["is", "the", "of", "and", "to"]
        expected_stop_words = {"is", "the", "of", "and", "to"}
        stop_words = getStopWordsSet(stop_words_text)
        self.assertEqual(stop_words, expected_stop_words)


# Test for if stop words are removed from words

class TestRemoveStopWords(unittest.TestCase):
    def test_remove_stop_words(self):
        stop_words = []
        with open("test-stopwords.txt", "r") as f:
            stop_words = [word.strip() for word in f.readlines()]
        with open("test-input-text.txt", "r") as f:
            text = f.read()
        words = get_top_words(text, stop_words)
        for stop_word in stop_words:
            self.assertNotIn(stop_word, words)

# More specific way to write same test

class TestRemoveStopWordsMoreSpecific(unittest.TestCase):
    def test_special_characters(self):
        stop_words = []
        with open("test-stopwords.txt", "r", encoding="utf8") as f:
            stop_words = [word.strip() for word in f.readlines()]
        with open("test-input-text.txt", "r", encoding="utf8") as f:
            text = f.read()
        words = get_top_words(text, stop_words)
        self.assertEqual(
            words, [('jumped', 2), ('over', 1), ('and', 1), ('into', 1), ('sea', 1)])


if __name__ == "__main__":
    unittest.main()
