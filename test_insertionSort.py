import unittest
from insertion_sort import insertionSort

class TestInsertionSort(unittest.TestCase):

    def test_insertionSort(self):

        input_data = [5, 3, 6, 4]
        actual_result = [3, 4, 5, 6]
        result = insertionSort(input_data)
        self.assertEqual(result, actual_result)

        input_data = []
        result = insertionSort(input_data)
        self.assertEqual(result, input_data)

if __name__ == '__main__':
    unittest.main()