import random


def select_sort(data):
    for x in range(len(data) - 1):
        min_index = x
        for y in range(x + 1, len(data)):
            if data[y] < data[min_index]:
                min_index = y
        data[x], data[min_index] = data[min_index], data[x]


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
select_sort(data_list)
print(data_list)