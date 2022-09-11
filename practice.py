# import sys

# n = int(sys.stdin.readline().rstrip())
# array = []

# for _ in range(n):
#     array.append(int(sys.stdin.readline().rstrip()))

# for _ in range(n):
#     for i in range(n - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]

# for number in array:
#     print(number)

import sys
n = int(sys.stdin.readline().rstrip())
count_array = [0] * 10001

for i in range(n):
    count_array[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if count_array[i] != 0:
        for j in range(count_array[i]):
            print(i)
