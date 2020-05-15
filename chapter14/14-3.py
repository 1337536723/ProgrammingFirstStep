from Utilities import swap


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)
    return


# 下面是调用代码，在书中应该独立形成一个代码块

arr = [3, 9, 4, 11, 7]
bubble_sort(arr)
print(arr)
