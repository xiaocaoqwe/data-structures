import random


def insert_sort(data):
    for x in range(len(data) - 1):
        for y in range(x + 1, 0, -1):
            if data[y] < data[y - 1]:
                data[y], data[y - 1] = data[y - 1], data[y]
            else:
                break


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
insert_sort(data_list)
print(data_list)