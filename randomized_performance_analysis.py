import random
import time

# Randomized Quicksort Function
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Performance Analysis
def performance_analysis():
    input_sizes = [10, 100, 1000, 10000]
    for size in input_sizes:
        print(f"\nInput Size: {size}")
        arr = random.sample(range(size * 10), size)  # Random array
        print(f"Random Array: {measure_time(randomized_quicksort, arr)} seconds")

        arr_sorted = sorted(arr)  # Sorted array
        print(f"Sorted Array: {measure_time(randomized_quicksort, arr_sorted)} seconds")

        arr_reverse_sorted = sorted(arr, reverse=True)  # Reverse sorted array
        print(f"Reverse Sorted Array: {measure_time(randomized_quicksort, arr_reverse_sorted)} seconds")

# Measure Time
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return round(end_time - start_time, 5)

# Run Performance Analysis
performance_analysis()
