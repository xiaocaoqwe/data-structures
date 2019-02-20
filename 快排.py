import random


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] > tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] < tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left

data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
quick_sort(data_list, 0, len(data_list)-1)
print(data_list)