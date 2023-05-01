import concurrent
import datetime
from collections import deque
from random import randint

import pandas as pd

from src.boyer_moore.boyer_moore_search import boyer_moore_search
from src.kmp.kmp_search import kpm_search
from src.rabin_karp.rabin_karp_search import rabin_karp_search

STARTING_UNICODE_CHARACTER = 48


def take_algorithm_time(item, func):
    """
    Calculates the time taken for the algorithm to sort the array. The result is in microseconds

    Parameters
    ----------
        item : list
            The array for sorting
        func : function
            search algorithm to test
    Returns
    ----------
        list : int
            The median taken for the algorithm to search the array (microseconds)
    """

    start_time = datetime.datetime.now()
    func(item[0], item[1])
    finish_time = datetime.datetime.now()
    full_time = finish_time - start_time
    return full_time.microseconds


def take_median_time_algorithm(algorithm, string_data):
    """
    Returns the median time for the sorting algorithm given

    Parameters
    ----------
        :param algorithm: Algorithm to process
        :param string_data : list[list]
            The arrays for sorting
    Returns
    ----------
        list : int
            The median taken for the algorithm to sort the samples set

    """
    times = []

    for item in string_data:
        times.append(take_algorithm_time(item, algorithm))

    df = pd.DataFrame(times)
    return df.median()


def get_search_data(string_array):
    """
    Returns the sorting time for a sample of arrays

    Parameters
    ----------
        :param string_array : list[list]
            The array for searching
    Returns
    ----------
        list : list
            A list with the time taken for boyer_moore, kmp and rabin_karp
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # submit the functions to the executor for parallel execution
        future1 = executor.submit(take_median_time_algorithm, boyer_moore_search, string_array)
        future2 = executor.submit(take_median_time_algorithm, kpm_search, string_array)
        future3 = executor.submit(take_median_time_algorithm, rabin_karp_search, string_array)

    # get the results of the executed functions
    result1 = future1.result()
    result2 = future2.result()
    future3 = future3.result()

    executor.shutdown()

    return [
        result1,
        result2,
        future3
    ]


def get_string_search_time(samples, length, alphabet_size, pattern_size):
    """
    Returns the time median time for the sorting algorithms with the defined parameters

    Parameters
    ----------
        :param samples : int
            The length of every array on the sample
        :param length : int
            The length of every array on the sample
        :param alphabet_size: Size of the alphabet to search for
    Returns
    ----------
        list : list
            A list with the time taken for boyer_moore, kpm and rabin_karp

    """

    string_array = deque()
    for i in range(samples):
        string, pattern = get_random_strings(length, pattern_size, alphabet_size)
        string_array.append((string, pattern))
    return get_search_data(string_array)


def get_random_strings(size, pattern_size, alphabet_size):
    ans = ""

    for i in range(size):
        value = randint(STARTING_UNICODE_CHARACTER, STARTING_UNICODE_CHARACTER + alphabet_size)
        ans += chr(value)

    value = randint(0, size - pattern_size)
    pattern = ans[value:value + pattern_size]
    return ans, pattern
