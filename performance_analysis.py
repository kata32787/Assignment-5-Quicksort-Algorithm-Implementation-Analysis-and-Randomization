import sys
import time
import random

# Increase recursion depth for recursive Quicksort
sys.setrecursionlimit(10000)

# Iterative Quicksort
def deterministic_quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Performance Analysis
def performance_analysis():
    # Input sizes for testing
    input_sizes = [10, 100, 1000, 10000]
    random_array = lambda n: [random.randint(1, 1000) for _ in range(n)]
    sorted_array = lambda n: list(range(1, n + 1))
    reverse_sorted_array = lambda n: list(range(n, 0, -1))

    print("Performance Analysis of Deterministic Quicksort (Iterative)")
    print("----------------------------------------------------------\n")

    for size in input_sizes:
        arr_random = random_array(size)
        arr_sorted = sorted_array(size)
        arr_reverse_sorted = reverse_sorted_array(size)

        print(f"Input Size: {size}")
        for test_array, array_type in zip(
            [arr_random, arr_sorted, arr_reverse_sorted],
            ["Random", "Sorted", "Reverse Sorted"]
        ):
            test_copy = test_array[:]  # Avoid modifying the original
            start_time = time.time()
            deterministic_quicksort_iterative(test_copy)
            elapsed_time = time.time() - start_time
            print(f"{array_type} Array: {elapsed_time:.5f} seconds")
        print("\n")

# Run the performance analysis
if __name__ == "__main__":
    performance_analysis()
