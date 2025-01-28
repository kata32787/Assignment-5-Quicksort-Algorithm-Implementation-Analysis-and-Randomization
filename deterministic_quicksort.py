# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:  # Base case
        return arr
    else:
        pivot = arr[0]  # Select the first element as pivot
        # Partitioning the array
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively apply Quicksort
        return deterministic_quicksort(less_than_pivot) + [pivot] + deterministic_quicksort(greater_than_pivot)

# Example usage with the specified array
if __name__ == "__main__":
    arr = [20, 90, 40, 10, 70, 5]
    print("Original Array:", arr)
    sorted_arr = deterministic_quicksort(arr)
    print("Sorted Array (Deterministic Quicksort):", sorted_arr)
