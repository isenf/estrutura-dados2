"""
Bubble sort algorithm.

Author: Dante Fabro.
Sep, 2026.
"""

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

def bubble_sort(A: list) -> None:
    """
    Sorts a list using Bubble Sort algorithm.

    Parameters
    ----------
    A: list
        Array like to be sorted.
    """
    n = len(A)

    for i in range(n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

# %%

arr = [9, 1, 0, 4, 6, 2]
print("unsorted:", arr)
bubble_sort(arr)
print("sorted:", arr)

