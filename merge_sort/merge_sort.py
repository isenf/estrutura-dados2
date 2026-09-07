"""
Merge sort algorithm.

Author: Dante Fabro.
Sep, 2026.
"""
# %%

def merge(left: list, right: list) -> list:
    """
    Merges two pre-sorted arrays into a single sorted array.

    Parameters
    ----------
    left: list
        Left array like.
    right: list
        Right array like.

    Returns
    -------
    list
        Sorted array with all elements from left and right.
    """
    arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j+= 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr

# %%

def merge_sort(A: list) -> list:
    """
    Sorts a list using Merge Sort algorithm.

    Parameters
    ----------
    A: list
        Array like to be sorted.
    
    Returns
    -------
    list
        Sorted array.
    """
    if len(A) <= 1: # base case: 1 size array (already sorted)
        return A

    # recursive cases
    half = len(A)//2
    left = merge_sort(A[:half])
    right = merge_sort(A[half:])

    return merge(left, right)

# %%

if __name__ == '__main__':
    arr = [9, 1, 0, 4, 6, 2]
    print("unsorted:", arr)
    sorted_arr = merge_sort(arr)
    print("sorted:", sorted_arr)
