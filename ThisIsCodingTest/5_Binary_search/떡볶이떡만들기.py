
def binary_search(array, target, start, end):
    memory = -1
    cnt = 0
    while start <= end: 
        cnt += 1
        print(f'{cnt} times')
        mid = (start + end) // 2
        print('start, mid, end: ', start, mid, end)
        length = 0
        for i in range(len(array)):
            if array[i] >= mid:
                length += array[i] - mid
        print('length: ', length)
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
array = list(map(int, input().split()))

result = binary_search(array, m, 0, max(array))
print(result)
    