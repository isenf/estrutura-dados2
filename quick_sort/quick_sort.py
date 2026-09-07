"""
Merge sort algorithm.

Author: Dante Fabro.
Sep, 2026.
"""
# %%

def quick_sort(A: list) -> list:
    """
    Sorts a list using Quick Sort algorithm.

    Parameters
    ----------
    A: list
        Array like to be sorted.
    
    Returns
    -------
    list
        Sorted array.
    """
    if len(A) <= 1: # base case
        return A

    pivot = A[len(A)//2]
    left = []
    middle = []
    right = []

    for elem in A:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            right.append(elem)

    return quick_sort(left) + middle + quick_sort(right)

# %%

if __name__ == '__main__':
    arr = [9, 1, 0, 4, 6, 2]
    print("unsorted:", arr)
    new_arr = quick_sort(arr)
    print("sorted:", new_arr)

