import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sorting import bubble_sort, selection_sort, insertion_sort

class SortingVisualizer:
    def __init__(self, algorithm='bubble'):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.algorithm = algorithm
        self.array = np.random.randint(1, 100, 20)  # Generate random array
        self.bars = self.ax.bar(range(len(self.array)), self.array)
        self.ax.set_title(f'{algorithm.title()} Sort Visualization')
        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('Value')
        
        # Initialize animation variables
        self.generator = None
        self.ani = None
        
    def update(self, frame):
        # Update the bar heights
        for bar, height in zip(self.bars, frame):
            bar.set_height(height)
        return self.bars
    
    def bubble_sort_generator(self):
        arr = self.array.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield arr.copy()
    
    def selection_sort_generator(self):
        arr = self.array.copy()
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr.copy()
    
    def insertion_sort_generator(self):
        arr = self.array.copy()
        n = len(arr)
        
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
            yield arr.copy()
    
    def start_animation(self):
        if self.algorithm == 'bubble':
            self.generator = self.bubble_sort_generator()
        elif self.algorithm == 'selection':
            self.generator = self.selection_sort_generator()
        elif self.algorithm == 'insertion':
            self.generator = self.insertion_sort_generator()
        
        self.ani = animation.FuncAnimation(
            self.fig, 
            self.update, 
            frames=self.generator,
            interval=100,  # Animation speed (ms)
            repeat=False,
            blit=True
        )
        plt.show()

def main():
    # Example usage
    visualizer = SortingVisualizer(algorithm='bubble')
    visualizer.start_animation()

if __name__ == "__main__":
    main() 