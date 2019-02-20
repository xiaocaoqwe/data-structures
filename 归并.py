import random


def merge_sort(data, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(data, low, mid)
        merge_sort(data, mid+1, high)
        merge(data, low, mid, high)


def merge(data, low, mid, high):
    i = low
    j = mid+1
    ltmp = []
    while i <= mid and j <= high:
        if data[i] < data[j]:
            ltmp.append(data[i])
            i += 1
        else:
            ltmp.append(data[j])
            j += 1
    while i <= mid:
        ltmp.append(data[i])
        i += 1
    while j <= high:
        ltmp.append(data[j])
        j += 1
    data[low:high+1] = ltmp


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
merge_sort(data_list, 0, len(data_list)-1)
print(data_list)