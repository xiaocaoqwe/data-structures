def bin_search(data, value):
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left+right)//2
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            right = mid - 1
        else:
            left = mid + 1


data_list = list(range(100))
print(bin_search(data_list, 54))