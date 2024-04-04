import unittest
from selection_sort import selectionSort

class TestSelectionSort(unittest.TestCase):

    def test_selectionSort(self):

        input_data = [5, 3, 6, 4]
        actual_result = [3, 4, 5, 6]
        result = selectionSort(input_data)
        self.assertEqual(result, actual_result)

        input_data = []
        result = selectionSort(input_data)
        self.assertEqual(result, input_data)

if __name__ == '__main__':
    unittest.main()