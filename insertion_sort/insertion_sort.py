"""
Insertion sort algorithm.

Author: Dante Fabro 
Sep, 2026.
"""
# %% [markdown]
# ## Insertion Sort

# %%
import matplotlib.pyplot as plt
import random
import time

# %%

def insertion_sort(A: list) -> None:
    for i in range(len(A)):
        key = A[i]
        j = i-1

        while(j >= 0 and A[j] > A[i]):
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

# %%

# test of insertion sort 
arr = ["Ana", "João", "Bia", "Carlos"]
print('unsorted:', arr)
insertion_sort(arr)
print('sorted:', arr)

# %%
random.seed(186) # for reproducibility
sizes = [100*i for i in range(1, 15+1)]
times = {
    'random': [],
    'sorted': []
}

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    start_time = time.time()
    insertion_sort(A=arr)
    end_time = time.time()

    times['random'].append(end_time-start_time)

    start_time = time.time()
    insertion_sort(A=arr)
    end_time = time.time()

    times['sorted'].append(end_time-start_time)

# %%

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(sizes, times['random'], label='random')
ax.plot(sizes, times['sorted'], label='sorted')
ax.set_xticks(ticks=sizes)
ax.set_xlabel("size of array")
ax.set_ylabel("execution time")
ax.set_title("complexity of insertion sort")
ax.legend()
plt.show()
