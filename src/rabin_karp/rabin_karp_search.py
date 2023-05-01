# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256


# pat  -> pattern
# txt  -> text
# q    -> A prime number


"""
    O(m) + O(m*n) --> O(m*n) for worst case
    Average is O(n)
"""
def rabin_karp_search(txt, pat, q=101):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M - 1):
        h = (h * d) % q

    positions = []

    # Calculate the hash value of pattern and first window
    # of text
    """
        O(m)
    """
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    """
        O(n-m) * O(m) --> O(m*n) + O(m^2) --> O(m*n)
    """
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                positions.append(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q

    return positions

# This code is contributed by Bhavya Jain
