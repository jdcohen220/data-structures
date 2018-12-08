from unittest import TestCase
from quicksort import *


class TestQuicksort(TestCase):

    def test_quicksort(self):
        array = [4, 2, 8, 9]
        expected = [2, 4, 8, 9]
        actual = Quicksort.quicksort(array)
        self.assertEqual(actual, expected)


        array2 = [1,0,9,3,7,8,2,8,3,9]
        expected2 = [0,1,2,3,3,7,8,8,9,9]
        actual2 = Quicksort.quicksort(array2)
        self.assertEqual(expected2, actual2)
