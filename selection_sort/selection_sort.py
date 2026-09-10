"""
Selection sort algorithm.

Author: Dante Fabro 
Sep, 2026.
"""

# %% [markdown]

# ## Selection Sort

# %%

import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# %%

def swap(arr: list, idx1: int, idx2: int) -> None:
    """
    Swaps two elements.

    Parameters
    ----------
    arr: list
        List with elements.
    idx1: int
        First element index.
    idx2: int
        First element index.
    """
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# %%

def selection_sort(arr: list) -> None:
    """
    Sorts a list using Selection Sort algorithm.

    Parameters
    ----------
    arr: list
        Array like to be sorted.
    """

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        swap(arr, i, min_idx)

# %%

def bidirectional_selection_sort(arr: list) -> None:
    """
    Implements the bidirectional invariant of the Selection Sort algorithm.

    Parameters
    ----------
    arr: list
        Array like to be sorted.
    """
    left = 0
    right = len(arr)-1

    while left < right:
        min_idx = left
        max_idx = left

        for j in range(left+1, right+1):
            if arr[min_idx] > arr[j]:
                min_idx = j
            if arr[max_idx] < arr[j]:
                max_idx = j

        swap(arr, left, min_idx)
        if(max_idx == left):
            max_idx = min_idx

        swap(arr, right, max_idx)
        left += 1
        right -= 1

# %%

def stable_selection_sort(arr: list):
    """
    Stable selection sort algorithm.

    arr: 
    """
    n = len(arr)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            min_val = arr[min_idx]
            for k in range(min_idx, i,-1):
                arr[k] = arr[k-1]
            arr[i] = min_val


# %%

def compute_time(alg: function, arr: list) -> float:
    """
    Compute the time to sort an array with an given function.

    Parameters
    ----------
    alg: function
        Sorting function.
    arr: list
        List to be sorted.

    Returns
    -------
    float
        Time spent on sorting.
    """
    start_time = time.time()
    alg(arr)
    end_time = time.time()

    return end_time - start_time


# %%

if __name__ == '__main__':
    # arr = ["Ana", "João", "Bia", "Carlos"]
    # # arr = [0, 3, -9,  1, 5, 7, 8]
    # print(f"original array: {arr}")
    # stable_selection_sort(arr)
    # print(f"sorted array: {arr}")
    # %%
    # vizualization of time
    random.seed(186) # for reproducibility
    sizes = [100*i for i in range(1, 15+1)]
    algs = {
        'default': selection_sort,
        'bidirectional': bidirectional_selection_sort,
        'stable': stable_selection_sort
    }
    times = {
        'default': [[], []],
        'bidirectional': [[], []],
        'stable': [[], []]
    }
    
    for size in sizes:
        for alg_name, alg in algs.items():
            arr = [random.randint(0, 1000) for _ in range(size)]

            times[alg_name][0].append(compute_time(
                alg, arr
            ))
            times[alg_name][1].append(compute_time(
                alg, arr
            ))
    
    # %%
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(sizes, times['default'][0], label='default')
    ax.plot(sizes, times['default'][1], label='default', linestyle='--')
    ax.plot(sizes, times['bidirectional'][0], label='bidirectional')
    ax.plot(sizes, times['bidirectional'][1], label='bidirectional', linestyle='--')
    ax.plot(sizes, times['stable'][0], label='stable')
    ax.plot(sizes, times['stable'][1], label='stable', linestyle='--')
    ax.set_xticks(ticks=sizes)
    ax.set_xlabel("size of array")
    ax.set_ylabel("execution time")
    ax.set_title("complexity of selection sort")
    ax.legend()
    plt.show()
