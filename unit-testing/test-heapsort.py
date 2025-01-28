import pytest
from heapsort import heapsort

def test_heapsort_empty_array():
    arr = []
    heapsort(arr)
    assert arr == []

def test_heapsort_single_element():
    arr = [5]
    heapsort(arr)
    assert arr == [5]

def test_heapsort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_heapsort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_heapsort_duplicate_elements():
    arr = [2, 4, 2, 1, 4]
    heapsort(arr)
    assert arr == [1, 2, 2, 4, 4]

def test_heapsort_negative_numbers():
    arr = [-5, -2, 0, 2, 5]
    heapsort(arr)
    assert arr == [-5, -2, 0, 2, 5]

def test_heapsort_invalid_input():
    with pytest.raises(TypeError):
        heapsort("hello")
