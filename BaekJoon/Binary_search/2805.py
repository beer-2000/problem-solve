from collections import Counter
from sys import stdin

def binary_search(array, target, start, end):
    memory = 0
    while start <= end:
        mid = (start + end) // 2
        length = 0
        # for i in range(len(array)):
        #     if array[i] > mid:
        #         length += array[i] - mid
        for i in array.keys():
            if i > mid:
                length += (i - mid) * array[i]
        if length == target:
            memory = mid
            return memory
        elif length > target:
            memory = mid
            start = mid + 1
        else:
            end = mid - 1
    return memory

n, m = map(int, input().split())
array = Counter(list(map(int, stdin.readline().split())))
# print(array)

result = binary_search(array, m, 0, max(array))

print(result)
        