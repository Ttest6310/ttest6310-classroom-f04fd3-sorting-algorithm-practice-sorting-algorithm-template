from sorting import insertion_sort

def test_insertion_sort():
    assert insertion_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]
    assert insertion_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9] 