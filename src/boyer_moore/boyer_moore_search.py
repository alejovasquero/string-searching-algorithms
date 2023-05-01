from collections import defaultdict

"""
    Calculates the list of bad characters
    This lists contains the last occurrence of a element in the sequence
    Normally this sequence is the pattern to find
    When a mismatch occurs, then we need to move the sequence to the last occurrence of the mismatch element
    O(m) -> m being the length of the pattern
"""


def create_bad_pattern(sequence: str, m: int) -> dict:
    bad_char = defaultdict(lambda: -1)

    for i in range(m):
        bad_char[ord(sequence[i])] = i

    return bad_char

"""
    The time complexity of the worst case happens when all the elements in the list are the same
    And also if the pattern has the same character repeated
    sequence = AAAAAAAAAAAAAAA
    sequence to find = AAAA
    O(m*n) + O(m) --> O(m*n)
"""


def boyer_moore_search(sequence: str, pattern: str) -> list[int]:
    n = len(sequence)
    m = len(pattern)

    """
        Preprocessing for bad characters
    """
    bad_character = create_bad_pattern(sequence, m)

    sequence_index = 0

    positions = []

    while sequence_index <= n - m:
        pattern_index = m - 1

        # We need to search from right to left
        while pattern_index >= 0 and pattern[pattern_index] == sequence[sequence_index + pattern_index]:
            pattern_index -= 1

        if pattern_index < 0:
            # This is a match :)
            positions.append(sequence_index)
            sequence_index += m - bad_character[ord(sequence[sequence_index + m])] if sequence_index + m < n else 1

        else:
            sequence_index += max(1, pattern_index - bad_character[ord(sequence[sequence_index + pattern_index])])

    return positions
