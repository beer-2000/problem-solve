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
    array.append(input())

array = list(set(array))

# for i in range(n):
#     for j in range(i + 1, n):
#         if compare(array[i], array[j]) == 1:
#             array[i], array[j] = array[j], array[i]

array_sorted = quick_sort(array)

for i in array_sorted:
    print(i)
