def quick_sort(num, low, high):
    if low >= high:
        return
    pivot_index = partition(num, low, high)
    quick_sort(num, low, pivot_index - 1)
    quick_sort(num, pivot_index + 1, high)


def partition(num, low, high):
    pivot_index = (low + high) // 2
    swap(num, pivot_index, high)
    i = low
    for j in range(low, high):
        if num[j] < num[high]:
            swap(num, i, j)
            i += 1
    swap(num, i, high)

    return i


def swap(num, i, j):
    temp = num[i]
    num[i] = num[j]
    num[j] = temp


num = [-1, -2, 0, 1, 0, -1, -2]
quick_sort(num, 0, len(num) - 1)
print(num)
