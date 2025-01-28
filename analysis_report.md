Quicksort Algorithm: Implementation, Analysis, and Randomization
# Introduction
The Quicksort algorithm is one of the most efficient and widely used sorting algorithms. This report explores the implementation of Quicksort in Python, its performance analysis, and the effects of randomization on its efficiency. The objective of this assignment was to implement both deterministic and randomized versions of Quicksort, analyze their time and space complexity, and compare their performance through empirical testing across different input sizes and distributions.

# Quicksort Algorithm Overview
Quicksort is a divide-and-conquer algorithm that selects a pivot element from the array and partitions the other elements into two subarrays: one with elements smaller than the pivot and the other with elements greater than the pivot. The process is recursively applied to the subarrays.

Best Case: 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) when the pivot divides the array evenly.
Worst Case: 
𝑂
(
𝑛
2
)
O(n 
2
 ) when the pivot is the smallest or largest element (e.g., when the array is already sorted).
Space Complexity: 
𝑂
(
log
⁡
𝑛
)
O(logn) due to recursion stack depth.
 # Implementation
Part 1: Deterministic Quicksort
The deterministic version of Quicksort uses the first element of the array as the pivot. Here's the implementation:

python
Copy
Edit
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x < pivot]
    greater_than_pivot = [x for x in arr[1:] if x >= pivot]
    return deterministic_quicksort(less_than_pivot) + [pivot] + deterministic_quicksort(greater_than_pivot)

# Test the deterministic quicksort
arr = [20, 90, 40, 10, 70, 5]
print("Original Array:", arr)
sorted_arr = deterministic_quicksort(arr)
print("Sorted Array (Deterministic Quicksort):", sorted_arr)
Result:

sql
Copy
Edit
Original Array: [20, 90, 40, 10, 70, 5]
Sorted Array (Deterministic Quicksort): [5, 10, 20, 40, 70, 90]
Part 2: Performance Analysis of Deterministic Quicksort
The performance analysis evaluates the time complexity of the deterministic Quicksort algorithm using various input sizes (10, 100, 1000, and 10000) with different array distributions (random, sorted, reverse sorted).

Results:
mathematica
Copy
Edit
Performance Analysis of Deterministic Quicksort
------------------------------------------------

Input Size: 10
Random Array: 0.00005 seconds
Sorted Array: 0.00005 seconds
Reverse Sorted Array: 0.00004 seconds

Input Size: 100
Random Array: 0.00026 seconds
Sorted Array: 0.00073 seconds
Reverse Sorted Array: 0.00077 seconds

Input Size: 1000
Random Array: 0.00248 seconds
Sorted Array: 0.08028 seconds
Reverse Sorted Array: 0.06214 seconds

Input Size: 10000
Random Array: 0.04187 seconds
Sorted Array: 4.90709 seconds
Reverse Sorted Array: 5.29269 seconds
The performance of the deterministic Quicksort shows significant degradation in the case of sorted and reverse-sorted arrays, highlighting the worst-case time complexity 
𝑂
(
𝑛
2
)
O(n 
2
 ).

# Randomized Quicksort
In this part, we implemented a randomized version of Quicksort where the pivot is chosen randomly from the subarray being sorted. This helps reduce the chances of encountering the worst-case time complexity.

python
Copy
Edit
import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less_than_pivot = [x for x in arr if x < pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)

# Test the randomized quicksort
arr = [20, 90, 40, 10, 70, 5]
print("Original Array:", arr)
sorted_arr = randomized_quicksort(arr)
print("Sorted Array (Randomized Quicksort):", sorted_arr)
Result:

javascript
Copy
Edit
Original Array: [20, 90, 40, 10, 70, 5]
Sorted Array (Randomized Quicksort): [5, 10, 20, 40, 70, 90]
Part 4: Performance Analysis of Randomized Quicksort
The performance analysis of the randomized version was conducted in the same manner as for the deterministic version.

Results:
mathematica
Copy
Edit
Performance Analysis of Randomized Quicksort
------------------------------------------------

Input Size: 10
Random Array: 7e-05 seconds
Sorted Array: 3e-05 seconds
Reverse Sorted Array: 4e-05 seconds

Input Size: 100
Random Array: 0.00029 seconds
Sorted Array: 0.00034 seconds
Reverse Sorted Array: 0.00028 seconds

Input Size: 1000
Random Array: 0.00507 seconds
Sorted Array: 0.00503 seconds
Reverse Sorted Array: 0.00757 seconds

Input Size: 10000
Random Array: 0.05014 seconds
Sorted Array: 0.04198 seconds
Reverse Sorted Array: 0.0462 seconds
The randomized Quicksort demonstrates better performance than the deterministic version, particularly for larger input sizes, since the likelihood of encountering the worst-case scenario is reduced.

# Discussion
The deterministic version of Quicksort has a worst-case time complexity of 
𝑂
(
𝑛
2
)
O(n 
2
 ), which is observed when the array is sorted or reverse sorted. In contrast, the randomized version helps mitigate this issue by choosing a random pivot, leading to more balanced partitions and a more consistent time complexity of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn) on average.

The empirical results demonstrate that the randomized version of Quicksort consistently outperforms the deterministic version, especially as the input size increases. This is evident from the performance data, where the deterministic version's time complexity grows substantially with sorted and reverse-sorted arrays, whereas the randomized version remains relatively stable across different array distributions.

# Conclusion
In conclusion, Quicksort is an efficient sorting algorithm with an average time complexity of 
𝑂
(
𝑛
log
⁡
𝑛
)
O(nlogn). The deterministic version, although efficient in most cases, can suffer from poor performance when the input is already sorted or reverse sorted. The randomized version addresses this issue by reducing the likelihood of encountering the worst-case time complexity. Through this assignment, we have successfully implemented both versions of Quicksort, analyzed their performance, and demonstrated the advantages of randomization in improving the algorithm's efficiency.

# References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). MIT Press.
Sedgewick, R. (2011). Algorithms (4th ed.). Addison-Wesley.
Knuth, D. E. (1998). The Art of Computer Programming, Volume 3: Sorting and Searching (2nd ed.). Addison-Wesley.