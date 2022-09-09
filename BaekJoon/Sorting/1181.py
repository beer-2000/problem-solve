import sys

def compare(s1, s2):
    if len(s1) < len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1
    elif s1 < s2:
        return 0
    else:
        return 1

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if compare(x, pivot) == 0]
    right_side = [x for x in tail if compare(x, pivot) == 1]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

n = int(input())

array = []
for i in range(n):
    array.append(sys.stdin.readline().rstrip())

array = list(set(array))

array_sorted = quick_sort(array)

## 시간 초과
# for i in range(len(array)):
#     for j in range(i + 1, len(array)):
#         if compare(array[i], array[j]) == 1:
#             array[i], array[j] = array[j], array[i]

for i in array_sorted:
    print(i)

# --------------------------------
# import sys
# n = int(input())

# array = []
# for i in range(n):
#     array.append(sys.stdin.readline().rstrip())

# array = sorted(list(set(array)))
# # array_sorted = sorted(array, key = lambda x: len[x])
# array.sort(key = lambda x: len(x))

# for word in array:
#     print(word)
