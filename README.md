# Sorting Algorithm Visualization Assignment

This assignment requires you to implement and visualize three basic sorting algorithms: bubble sort, selection sort, and insertion sort. You will create an animated demonstration that shows how each algorithm works step by step.

## Requirements

1. Implement the following sorting algorithms in the `sorting.py` file:
   - `bubble_sort(arr)`: Bubble sort
   - `selection_sort(arr)`: Selection sort
   - `insertion_sort(arr)`: Insertion sort

2. Create a visualization module `visualization.py` that demonstrates each sorting algorithm with the following features:
   - Animated step-by-step execution of the sorting process
   - Visual representation of array elements (e.g., bars of different heights)
   - Highlighting of elements being compared or swapped
   - Clear indication of sorted and unsorted portions of the array
   - Controls to start, pause, and reset the visualization
   - Option to adjust animation speed

3. All sorting functions should accept a list as input and return a new sorted list without modifying the original list.

## Algorithm Descriptions

### Bubble Sort
- Bubble sort works by repeatedly traversing the list to be sorted, comparing adjacent items and swapping them if they are in the wrong order
- The traversal is repeated until no swaps occur, indicating the list is sorted
- Visualization should highlight the current pair being compared and show swaps in real-time

### Selection Sort
- Selection sort works by finding the minimum element from the unsorted portion and putting it at the end of the sorted portion
- This process is repeated until all elements are sorted
- Visualization should highlight the current minimum element and show the selection process

### Insertion Sort
- Insertion sort builds the sorted portion by inserting unsorted elements one by one into their correct positions
- Similar to arranging cards in your hand when playing poker
- Visualization should show the insertion process and shifting of elements

## Visualization Requirements

1. Use a graphical library of your choice (e.g., Pygame, Matplotlib, or Tkinter)
2. Create a clear and intuitive user interface
3. Include the following features:
   - Random array generation
   - Step-by-step execution
   - Play/pause controls
   - Speed adjustment
   - Reset functionality
   - Clear visual distinction between sorted and unsorted portions
   - Color coding for different operations (comparisons, swaps, etc.)

## Example Implementation

```python
# Example visualization structure
class SortingVisualizer:
    def __init__(self):
        self.array = []
        self.speed = 1.0
        self.is_running = False
        
    def generate_random_array(self, size):
        # Generate random array for visualization
        pass
        
    def visualize_sort(self, algorithm):
        # Animate the sorting process
        pass
        
    def update_display(self):
        # Update the visualization
        pass
```

## Grading Criteria

- Sorting algorithm implementation: 30 points
- Visualization implementation: 40 points
- User interface and controls: 20 points
- Code quality and documentation: 10 points
- Total: 100 points

## Submission Requirements

1. Complete the sorting algorithm implementations in `sorting.py`
2. Create the visualization module in `visualization.py`
3. Include a requirements.txt file with necessary dependencies
4. Provide clear instructions for running the visualization
5. Include a brief documentation of your visualization approach
6. Ensure all test cases pass

## Additional Notes

- Focus on making the visualization educational and easy to understand
- Consider adding explanatory text or annotations to help understand the algorithm steps
- Test your visualization with different array sizes and initial conditions
- Make sure the visualization runs smoothly and is responsive to user controls 
