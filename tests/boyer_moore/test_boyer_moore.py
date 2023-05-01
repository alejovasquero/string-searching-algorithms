import unittest
from src.boyer_moore.boyer_moore_search import boyer_moore_search


class KMPTest(unittest.TestCase):

    def test_should_search_string_kmp(self):
        result = boyer_moore_search("aabcaaa", "ab")
        self.assertEqual(result, [1])

        result = boyer_moore_search("aabcaaafajadaabkfakakaskaaabd", "aab")
        self.assertEqual(result, [0, 12, 25])


if __name__ == "__main__":
    unittest.TextTestRunner.run(unittest.TestLoader.loadTestsFromTestCase(KMPTest))
