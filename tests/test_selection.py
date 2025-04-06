from sorting import selection_sort

def test_selection_sort():
    assert selection_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert selection_sort([]) == []
    assert selection_sort([5]) == [5]
    assert selection_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5] 