"""
Selection sort algorithm.

Author: Dante Fabro 

Aug, 2026.
"""

# %% [markdown]

# ## Selection Sort

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

def selection_sort(A: list):
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

arr = ["Ana", "João", "Bia", "Carlos"]
# arr = [0, 3, -9,  1, 5, 7, 8]
print(f"original array: {arr}")
selection_sort(A=arr)
print(f"sorted array: {arr}")

