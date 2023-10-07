import unittest

def kth_largest_element(arr, k):
    if k <= 0 or k > len(arr):
        return None, None

    sorted_arr = sorted(arr, reverse=True)
    kth_largest = sorted_arr[k - 1]
    position = arr.index(kth_largest)

    return kth_largest, position

class TestKthLargestElement(unittest.TestCase):
    def test_kth_largest_element(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
