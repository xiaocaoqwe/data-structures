import random

def big_endian(data, start, end):
    i = start
    j = 2*i+1
    tmp = data[i]
    while j <= end:
        if j+1 <= end and data[j+1] > data[j]:
            j += 1
        if data[j] > tmp:
            data[i] = data[j]
            i = j
            j = 2*i+1
        else:
            break
    data[i] = tmp


def heap_sort(data):
    n = len(data)
    for x in range(n//2-1, -1, -1):
        big_endian(data, x, n-1)
    for x in range(n-1, -1, -1):
        data[0], data[x] = data[x], data[0]
        big_endian(data, 0, x-1)


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
heap_sort(data_list)
print(data_list)