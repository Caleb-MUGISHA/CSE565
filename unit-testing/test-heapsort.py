import unittest
from heapsort import heapsort

class HeapSortTests(unittest.TestCase):
    def test_handles_empty_list(self):
        # Verify empty list is handled correctly
        test_list = []
        heapsort(test_list)
        self.assertEqual(test_list, [])
        
    def test_sorts_single_value(self):
        # Verify single-element list remains unchanged
        test_list = [42]
        heapsort(test_list)
        self.assertEqual(test_list, [42])
        
    def test_maintains_presorted_sequence(self):
        # Verify already sorted list stays sorted
        test_list = [-10, 0, 5, 10, 20]
        expected = test_list.copy()
        heapsort(test_list)
        self.assertEqual(test_list, expected)
        
    def test_sorts_reverse_sequence(self):
        # Verify reverse-sorted list gets properly sorted
        test_list = [100, 75, 50, 25, 0]
        heapsort(test_list)
        self.assertEqual(test_list, [0, 25, 50, 75, 100])
        
    def test_sorts_random_sequence(self):
        # Verify random sequence gets properly sorted
        test_list = [42, 13, 7, 99, 24, 56, 33]
        heapsort(test_list)
        self.assertEqual(test_list, [7, 13, 24, 33, 42, 56, 99])
        
    def test_handles_repeated_values(self):
        # Verify list with duplicate values sorts correctly
        test_list = [5, 5, 3, 3, 1, 1, 4, 4]
        heapsort(test_list)
        self.assertEqual(test_list, [1, 1, 3, 3, 4, 4, 5, 5])
        
    def test_handles_mixed_numbers(self):
        # Verify mix of positive, negative, and zero values
        test_list = [-5, 0, 10, -15, 20, -25]
        heapsort(test_list)
        self.assertEqual(test_list, [-25, -15, -5, 0, 10, 20])

        ##My tests##
        
    def test_stress_large_sequence(self):
        # Verify sorting of large sequence
        size = 1000
        test_list = list(range(size, 0, -1))  # Create reverse sorted list
        expected = list(range(1, size + 1))   # Create properly sorted list
        heapsort(test_list)
        self.assertEqual(test_list, expected)
        
    def test_rejects_non_list(self):
        # Verify non-list inputs are rejected
        invalid_inputs = [
            "string",
            123,
            3.14,
            None,
            {'key': 'value'}
        ]
        for invalid_input in invalid_inputs:
            with self.assertRaises(TypeError):
                heapsort(invalid_input)
                
    def test_handles_all_same_value(self):
        # Verify list with all identical values
        test_list = [7] * 10
        heapsort(test_list)
        self.assertEqual(test_list, [7] * 10)

if __name__ == '__main__':
    unittest.main()