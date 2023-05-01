import unittest
from src.kmp.kmp_search import calculate_lps, kpm_search


class KMPTest(unittest.TestCase):

    def test_should_calculate_lps(self):
        lps = calculate_lps("abcdabcc")
        self.assertEqual(lps, [0, 0, 0, 0, 1, 2, 3, 0])

    def test_should_calculate_edge_lps(self):
        lps = calculate_lps("aabcaaa")
        self.assertEqual(lps, [0, 1, 0, 0, 1, 2, 2])

    def test_should_search_string_kmp(self):
        result = kpm_search("aabcaaa", "ab")
        self.assertEqual(result, [1])

        result = kpm_search("aabcaaafajadaabkfakakaskaaabd", "aab")
        self.assertEqual(result, [0, 12, 25])


if __name__ == "__main__":
    unittest.TextTestRunner.run(unittest.TestLoader.loadTestsFromTestCase(KMPTest))
