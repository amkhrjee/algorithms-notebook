import multiprocessing as mp
import random
import time


def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def radixsort(arr):
    for digit_index in range(len(str(max(arr)))):
        output = [0 for _ in range(len(arr))]
        digit_bucket = [0 for _ in range(10)]
        for each_item in arr:
            digit = (each_item // 10 ** digit_index) % 10
            digit_bucket[digit] += 1

        # prefix sum
        for i in range(1, 10):
            digit_bucket[i] += digit_bucket[i - 1]

        for each_num in reversed(arr):
            digit = (each_num // 10 ** digit_index) % 10
            output[digit_bucket[digit] - 1] = each_num
            digit_bucket[digit] -= 1
        arr = output
    return arr


def countingsort(arr):
    num_bucket = [0 for _ in range(max(arr) + 1)]
    for each_num in arr:
        num_bucket[each_num] += 1

    sorted_arr = []
    for i in range(len(num_bucket)):
        if num_bucket[i] > 0:
            sorted_arr.extend([i for _ in range(num_bucket[i])])

    return sorted_arr


def random_partition(arr, start_index, end_index):
    i = random.randint(start_index, end_index)
    arr[i], arr[end_index] = arr[end_index], arr[i]
    return partition(arr, start_index, end_index)


def partition(arr, start_index, end_index):
    x = arr[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end_index] = arr[end_index], arr[i + 1]
    return i + 1


def quicksort(arr, start_index, end_index):
    if start_index < end_index:
        pivot_index = random_partition(arr, start_index, end_index)
        quicksort(arr, start_index, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end_index)


def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergesort(left_half)
    right_half = mergesort(right_half)
    return merge(left_half, right_half)


def heapsort(arr):
    import heapq
    heapq.heapify(arr)
    sorted_arr = []
    while len(arr):
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr


def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        min = float('inf')
        for j in range(i, n):
            if arr[j] < min:
                min = arr[j]
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        max = -float('inf')
        for j in range(n - i):
            if arr[j] > max:
                max = arr[j]
                max_index = j
        arr[max_index], arr[n - i - 1] = arr[n - i - 1], arr[max_index]
    return arr


bubble_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_arr = list(bubble_arr)


def bubblesort_worker(arr):
    start_time = time.perf_counter()
    bubblesort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def mergesort_worker(arr):
    start_time = time.perf_counter()
    mergesort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def selectionsort_worker(arr):
    start_time = time.perf_counter()
    selectionsort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def insertionsort_worker(arr):
    start_time = time.perf_counter()
    insertionsort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def heapsort_worker(arr):
    start_time = time.perf_counter()
    heapsort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def quicksort_worker(arr):
    start_time = time.perf_counter()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def radixsort_worker(arr):
    start_time = time.perf_counter()
    radixsort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def countingsort_worker(arr):
    start_time = time.perf_counter()
    countingsort(arr)
    end_time = time.perf_counter()
    time_function = end_time - start_time
    return time_function


def main():
    import matplotlib.pyplot as plt
    test_cases = 1000
    input_list = []

    bubble_time_list = []
    merge_time_list = []
    counting_time_list = []
    radix_time_list = []
    selection_time_list = []
    insertion_time_list = []
    heap_time_list = []
    quick_time_list = []

    for i in range(2, test_cases):
        input_list.append(i)
        with mp.Pool(8) as pool:
            bubble_arr = [random.randint(0, 1000) for _ in range(i)]
            merge_arr = list(bubble_arr)
            insertion_arr = list(bubble_arr)
            selection_arr = list(bubble_arr)
            radix_arr = list(bubble_arr)
            counting_arr = list(bubble_arr)
            quick_arr = list(bubble_arr)
            heap_arr = list(bubble_arr)

            async_bubblesort = pool.apply_async(
                bubblesort_worker, args=(bubble_arr, ))
            async_mergesort = pool.apply_async(
                mergesort_worker, args=(merge_arr, ))
            async_countingsort = pool.apply_async(
                countingsort_worker, args=(counting_arr, ))
            async_radixsort = pool.apply_async(
                radixsort_worker, args=(radix_arr, ))
            async_selectionsort = pool.apply_async(
                selectionsort_worker, args=(selection_arr, ))
            async_insertionsort = pool.apply_async(
                insertionsort_worker, args=(insertion_arr, ))
            async_heapsort = pool.apply_async(
                heapsort_worker, args=(heap_arr, ))
            async_quicksort = pool.apply_async(
                quicksort_worker, args=(quick_arr, ))

            bubble_time = async_bubblesort.get()
            bubble_time_list.append(bubble_time)

            merge_time = async_mergesort.get()
            merge_time_list.append(merge_time)

            quick_time = async_quicksort.get()
            quick_time_list.append(quick_time)

            heap_time = async_heapsort.get()
            heap_time_list.append(heap_time)

            insertion_time = async_insertionsort.get()
            insertion_time_list.append(insertion_time)

            selection_time = async_selectionsort.get()
            selection_time_list.append(selection_time)

            radix_time = async_radixsort.get()
            radix_time_list.append(radix_time)

            counting_time = async_countingsort.get()
            counting_time_list.append(counting_time)

    plt.figure(figsize=(30, 10))

    plt.plot(input_list, bubble_time_list, color="blue", label="Bubble sort")
    plt.plot(input_list, merge_time_list, color="orange", label="Merge sort")
    plt.plot(input_list, insertion_time_list,
             color="green", label="Insertion sort")
    plt.plot(input_list, selection_time_list,
             color="red", label="Selection sort")
    plt.plot(input_list, radix_time_list, color="black", label="Radix sort")
    plt.plot(input_list, heap_time_list, color="magenta", label="Heap sort")
    plt.plot(input_list, quick_time_list, color="pink", label="Quick sort")
    plt.plot(input_list, counting_time_list,
             color="aqua", label="Counting sort")

    plt.title("Performance Comparison of Sorting Algorithms (Run Parallely)")
    plt.xlabel("Number of integers")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
