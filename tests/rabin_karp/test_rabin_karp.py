import unittest
from src.rabin_karp.rabin_karp_search import rabin_karp_search


class KMPTest(unittest.TestCase):

    def test_should_search_string_kmp(self):
        result = rabin_karp_search("aabcaaa", "ab", 101)
        self.assertEqual(result, [1])

        result = rabin_karp_search("aabcaaafajadaabkfakakaskaaabd", "aab", 101)
        self.assertEqual(result, [0, 12, 25])


if __name__ == "__main__":
    unittest.TextTestRunner.run(unittest.TestLoader.loadTestsFromTestCase(KMPTest))
