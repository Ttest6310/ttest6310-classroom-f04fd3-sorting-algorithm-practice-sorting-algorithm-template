from sorting import bubble_sort

def test_bubble_sort():
    assert bubble_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5] 