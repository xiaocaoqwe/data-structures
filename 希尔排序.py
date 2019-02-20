import random


def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for x in range(gap, len(data)):
            for y in range(x, gap - 1, -gap):
                if data[y] < data[y - gap]:
                    data[y], data[y - gap] = data[y - gap], data[y]
                else:
                    break
        gap = gap // 2


data_list = list(range(10))
random.shuffle(data_list)
print(data_list)
shell_sort(data_list)
print(data_list)