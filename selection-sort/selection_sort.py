"""
Selection sort algorithm.

Author: Dante Fabro 
Aug, 2026.
"""

# %% [markdown]

# ## Selection Sort

# %%

import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# %%

def swap(A: list, idx1: int, idx2: int) -> None:
    """
    Swaps two elements.

    Parameters
    ----------
    A: list
        List with elements.
    idx1: int
        First element index.
    idx2: int
        First element index.
    """
    A[idx1], A[idx2] = A[idx2], A[idx1]

# %%

def selection_sort(A: list) -> None:
    """
    Sorts a list using Selection Sort algorithm.

    Parameters
    ----------
    A: list
        Array like to be sorted.
    """

    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        swap(A, i, min_idx)

# %%

def bidirectional_selection_sort(A: list) -> None:
    """
    Implements the bidirectional invariant of the Selection Sort algorithm.

    Parameters
    ----------
    A: list
        Array like to be sorted.
    """
    left = 0
    right = len(A)-1

    while left < right:
        min_idx = left
        max_idx = left

        for j in range(left+1, right+1):
            if A[min_idx] > A[j]:
                min_idx = j
            if A[max_idx] < A[j]:
                max_idx = j

        swap(A, left, min_idx)
        if(max_idx == left):
            max_idx = min_idx

        swap(A, right, max_idx)
        left += 1
        right -= 1

# %%

arr = ["Ana", "João", "Bia", "Carlos"]
# arr = [0, 3, -9,  1, 5, 7, 8]
print(f"original array: {arr}")
bidirectional_selection_sort(A=arr)
print(f"sorted array: {arr}")

# %%

# vizualization of time
random.seed(186) # for reproducibility
sizes = [100*i for i in range(1, 15+1)]
times = {
    'default': [],
    'minmax': []
}

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    selection_sort(A=arr)
    end_time = time.time()

    times['default'].append(end_time-start_time)

    start_time = time.time()
    bidirectional_selection_sort(A=arr)
    end_time = time.time()

    times['minmax'].append(end_time-start_time)

# %%

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(sizes, times['default'], label='default')
ax.plot(sizes, times['minmax'], label='bidirectional')
ax.set_xticks(ticks=sizes)
ax.set_xlabel("size of array")
ax.set_ylabel("execution time")
ax.set_title("complexity of selection sort")
ax.legend()
plt.show()
