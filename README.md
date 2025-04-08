# Sorting Algorithm Implementation Assignment

This assignment requires you to implement three basic sorting algorithms: bubble sort, selection sort, and insertion sort.

## Requirements

1. Complete the implementation of the following functions in the `sorting.py` file:
   - `bubble_sort(arr)`: Bubble sort
   - `selection_sort(arr)`: Selection sort
   - `insertion_sort(arr)`: Insertion sort

2. All functions should accept a list as input and return a new sorted list without modifying the original list.

3. Your implementation will be graded through automated testing.

## Algorithm Descriptions

### Bubble Sort
- Bubble sort works by repeatedly traversing the list to be sorted, comparing adjacent items and swapping them if they are in the wrong order
- The traversal is repeated until no swaps occur, indicating the list is sorted

### Selection Sort
- Selection sort works by finding the minimum element from the unsorted portion and putting it at the end of the sorted portion
- This process is repeated until all elements are sorted

### Insertion Sort
- Insertion sort builds the sorted portion by inserting unsorted elements one by one into their correct positions
- Similar to arranging cards in your hand when playing poker

## Examples

### Input/Output Examples

```python
# Example 1
Input: [3, 1, 4, 2]
Output: [1, 2, 3, 4]

# Example 2
Input: []
Output: []

# Example 3
Input: [5]
Output: [5]
```

### Bubble Sort Example Implementation

```python
def bubble_sort_example(arr):
    # Create a copy of the input array to avoid modifying the original array
    result = arr.copy()
    n = len(result)
    
    # Outer loop: need to perform n-1 bubble passes
    for i in range(n):
        # Inner loop: compare adjacent elements and swap
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                # Swap elements
                result[j], result[j+1] = result[j+1], result[j]
    
    return result
```

## Grading Criteria

- Bubble sort implementation: 30 points
- Selection sort implementation: 30 points
- Insertion sort implementation: 30 points
- Total: 90 points

## Submission Requirements

1. Complete the function implementations in the `sorting.py` file
2. Ensure all test cases pass
3. Do not modify the test files or configuration files 
