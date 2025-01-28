import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Choose a random pivot index
        pivot_index = random.randint(0, len(arr) - 1)
        # Swap the chosen pivot with the first element
        arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Test the Randomized Quicksort algorithm
if __name__ == "__main__":
    test_array = [20, 90, 40, 10, 70, 5]
    print("Original Array:", test_array)
    sorted_array = randomized_quicksort(test_array)
    print("Sorted Array (Randomized Quicksort):", sorted_array)
