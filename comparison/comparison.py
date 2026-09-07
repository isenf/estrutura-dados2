"""
Comparison of sorting algorithms.

Author: Dante Fabro 
Sep, 2026.
"""
# %%

import time
import random
import seaborn as sns
import matplotlib.pyplot as plt
from bubble_sort.bubble_sort import bubble_sort
from merge_sort.merge_sort import merge_sort
from insertion_sort.insertion_sort import insertion_sort
from quick_sort.quick_sort import quick_sort
from selection_sort.selection_sort import selection_sort, bidirectional_selection_sort

# %%

sorting_algs = {
    'Bubble sort': bubble_sort,
    'Merge sort': merge_sort,
    'Insertion sort': insertion_sort,
    'Quick sort': quick_sort,
    'Selection sort': selection_sort,
    'Bidirectional selectionsort': bidirectional_selection_sort
}

# %%

def measure_time(alg, arr):
    """
    Measure the time of sort.

    Parameters
    ----------
    alg: function
        Sorting algorithm function.
    arr: list
        List to be sorted.

    Returns
    -------
    float
        Time spend sorting.
    """
    start_time = time.time()
    alg(arr)
    end_time = time.time()

    return end_time - start_time

# %%

def generate_arr(size, random_state=23):
    """
    Generate a random integer array.

    Parameters
    ----------
    size: int
        Size of array.
    random_state: int, optional
        Random seed. The default is 23.

    Returns
    -------
        Array with random integer.
    """
    random.seed(random_state)
    return [random.randint(0, 1000) for _ in range(size)]

# %%

if __name__ == '__main__':
    times = {}
    sizes = [100*i for i in range(1, 15+1)]

    for i, (alg_name, alg) in enumerate(sorting_algs.items()):
        aux =[]
        for size in sizes:
            arr = generate_arr(size, random_state=23+i)
            aux.append(measure_time(alg, arr))

        times[alg_name] = aux

    plt.style.use("dark_background")
    # sns.set_style("darkgrid")
    sns.set_context("talk", font_scale=0.8)
    sns.set_palette("plasma")
    fig, ax = plt.subplots(figsize=(15, 7))
    for alg_name in sorting_algs.keys():
        sns.lineplot(x=sizes, y=times[alg_name], 
                     label=alg_name, ax=ax)
    ax.grid(False)
    ax.set_xticks(sizes)
    ax.set_xlabel("size of array")
    ax.set_ylabel("execution time")
    ax.set_title("comparison between sorting algorithms")
    ax.legend()
    plt.show()

# %%
# plt.style.available
