from random import randint
import time
start_time = time.time()

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

array = []
for _ in range(10000):
    array.append(randint(1, 100))
# print(array)
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    # print((left_side + [pivot] + right_side))
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
print("time : ", time.time() - start_time)
