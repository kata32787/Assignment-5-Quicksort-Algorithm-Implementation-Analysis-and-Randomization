# Assignment-5-Quicksort-Algorithm-Implementation-Analysis-and-Randomization
Overview
This repository provides an implementation of the Quicksort algorithm along with performance analysis and randomization enhancements. The project is divided into three main tasks:

Implementing Deterministic Quicksort
Performing Performance Analysis of Deterministic Quicksort
Implementing Randomized Quicksort
Performing Performance Analysis of Randomized Quicksort
The objective is to understand how deterministic and randomized versions of Quicksort perform under different input sizes and distributions, and to compare the performance between the two approaches.
Instructions
Step 1: Set Up Your Environment
Ensure you have the following:

Python 3.6 or later installed on your machine.
No additional libraries are required for this project; it uses built-in Python libraries.
Step 2: Running the Tasks
Task 1: Implementing Deterministic Quicksort
In the deterministic_quicksort.py file, a basic implementation of Quicksort is provided.
This version uses the first element of the array as the pivot to partition the array and sort it recursively.
Run the file to sort a given array. The output will show the original array and the sorted array.

Task 2: Performance Analysis of Deterministic Quicksort
In performance_analysis.py, performance testing for the deterministic version of Quicksort is performed.
It runs tests for different array sizes (10, 100, 1000, 10000) and evaluates the sorting time for:
Random arrays
Sorted arrays
Reverse-sorted arrays
Run the script to see the performance results for each array size and distribution.
Task 3: Implementing Randomized Quicksort
In randomized_quicksort.py, a randomized version of Quicksort is implemented, where the pivot is chosen randomly to reduce the chance of worst-case time complexity.
Run the file to sort a sample array and compare the result to the deterministic Quicksort output.
Task 4: Performance Analysis of Randomized Quicksort
In randomized_performance_analysis.py, the randomized Quicksort is tested for performance with various array sizes and distributions.
It calculates the time taken for sorting random, sorted, and reverse-sorted arrays.
Run the script to obtain performance analysis results for randomized Quicksort.
Step 3: Report Generation
After running the performance analysis scripts, you can analyze the results.
The analysis_report.md file contains detailed analysis of the performance of both deterministic and randomized Quicksort. The report compares the execution time across different array sizes and sorting methods, highlighting the advantages of randomization.
Step 4: Review the Results
After running the performance analysis scripts for both deterministic and randomized Quicksort, you will have output showing how the algorithms perform under different conditions. The results should give insights into:

The time complexity for each algorithm under different input sizes.
How the randomized version mitigates the performance issues of the deterministic version when the array is already sorted or reverse sorted.
Step 5: Conclusion
Deterministic Quicksort may have poor performance when the array is sorted or reverse sorted.
Randomized Quicksort improves performance by reducing the likelihood of encountering the worst-case time complexity.
File Descriptions
deterministic_quicksort.py: Implements the deterministic Quicksort algorithm.
randomized_quicksort.py: Implements the randomized Quicksort algorithm.
performance_analysis.py: Contains performance analysis for deterministic Quicksort.
randomized_performance_analysis.py: Contains performance analysis for randomized Quicksort.
analysis_report.md: An in-depth report analyzing the results of the performance tests.