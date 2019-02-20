import random


def bubble_sort(data):
    for x in range(len(data) - 1):
        for y in range(len(data) - x - 1):
            if data[y] > data[y + 1]:
                data[y], data[y + 1] = data[y + 1], data[y]


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
bubble_sort(data_list)
print(data_list)