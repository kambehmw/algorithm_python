def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    print(quick_sort([10, 5, 2, 3]))
    print(quick_sort([-1, 6, 3, 10, 30, 23, 15]))