"""
    O(m) + O(n) = O(m+n)
"""


def kpm_search(sequence, sequence_to_find) -> list:
    # i for the sequence, j for the sequence to find
    i, j = 0, 0

    positions = []

    lps = calculate_lps(sequence_to_find)

    """
        O(n)
    """
    while i < len(sequence):
        if sequence[i] == sequence_to_find[j]:
            i += 1
            j += 1

        if j == len(sequence_to_find):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(sequence) and sequence[i] != sequence_to_find[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return positions


"""
    Calculates the lps (longest prefix suffix) for the pattern
    O(m)
"""
def calculate_lps(sequence) -> list:
    lps = [None] * len(sequence)

    # A prefix suffix of one element does not exist
    lps[0] = 0

    i = 1

    # lps[0] starting
    longest_prefix_suffix_before_i = 0

    while i < len(sequence):

        if sequence[i] == sequence[longest_prefix_suffix_before_i]:
            longest_prefix_suffix_before_i += 1
            lps[i] = longest_prefix_suffix_before_i
            i += 1

        else:
            if longest_prefix_suffix_before_i != 0:
                longest_prefix_suffix_before_i = lps[longest_prefix_suffix_before_i - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
