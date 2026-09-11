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
}

KINDS = ["random", "sorted", "reversed"]

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

def generate_arr(size, random_state=23, kind='random'):
    """
    Generate a random integer array.

    Parameters
    ----------
    size: int
        Size of array.
    random_state: int, optional
        Random seed. The default is 23.
    kind: str, optional
        The kind of arr to be generated, 
        possible values: random, sorted, reversed.
        The default is 'random'.

    Returns
    -------
        Array with random integer.
    """
    random.seed(random_state)

    if kind == "random":
        return [random.randint(0, 1000) for _ in range(size)]
    elif kind == "sorted":
        return list(range(size))
    elif kind == "reversed":
        arr = list(range(size, 0, -1))
    else:
        raise ValueError("unknown kind:", kind)

    return arr

# %%

def benchmark(
    algs: dict, 
    sizes: list[int], 
    kinds:list[str] =KINDS, 
    seed_base:int=23
):
    """
    Runs the algorithms and compute the times spent sorting.

    Parameters
    ----------
    algs: dict
        Key-value mapping with algorithm name and algorithm function.
    sizes: list[int]
        The sizes of array to be generated.
    kind: str, optional
        The kind of arrays. The default is 'random'.
    seed_base: int, optional
        Seed. The default is 23.

    Returns
    -------
    dict
        Dict with the computed time.
    """
    inputs = {
        kind: {
            size: generate_arr(size, random_state=seed_base, kind=kind)
            for size in sizes
        }
        for kind in kinds
    }

    res = {}
    for alg_name, alg in algs.items():
        res[alg_name] = {}
        for kind in kinds:
            aux = []
            for size in sizes:
                arr = inputs[kind][size].copy()
                aux.append(measure_time(alg, arr))
            res[alg_name][kind] = aux

    return res


# %%

def plot_comparison(sorting_algs: dict, sizes: list[int] = None, kinds:list[str]=KINDS):
    if sizes is None:
        sizes = [100*i for i in range(1, 15+1)]
    alg_times = benchmark(sorting_algs, sizes, kinds=kinds)

    plt.style.use("dark_background")
    # sns.set_style("darkgrid")
    sns.set_context("talk", font_scale=0.8)
    sns.set_palette("plasma")

    colors = plt.cm.plasma([i/len(sorting_algs) for i in range(len(sorting_algs))])
    color_map = dict(zip(sorting_algs.keys(), colors))

    n = len(kinds)
    fig, axes = plt.subplots(n, 1, figsize=(16, 8*n), sharey=False, sharex=True)

    if n == 1:
        axes = [axes]

    for kind, ax in zip(kinds, axes):
        for alg_name in sorting_algs.keys():
            ax.plot(sizes, alg_times[alg_name][kind], 
                    color=color_map[alg_name],
                    marker="*",
                    label=f"{alg_name}")
        ax.grid(False)
        ax.set_xticks(sizes)
        ax.set_xlabel("size of array")
        ax.set_ylabel("execution time")
        ax.set_title(f"input: {kind}")
        ax.legend()

    plt.suptitle("comparison between sorting algorithms")
    plt.show()


# %%
if __name__ == '__main__':
    plot_comparison(sorting_algs)

