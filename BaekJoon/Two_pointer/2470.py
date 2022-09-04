
n = int(input())
array = sorted(list(map(int, input().split())))
print(array)

left = 0
right = n - 1
min = abs(array[left] + array[right])
min_left = left
min_right = right

while left < right:
    print('left, right, min_left, min_right, min', left, right, min_left, min_right, min)
    print('array[left], array[right]: ', array[left], array[right])
    print('abs: ', abs(array[left] + array[right]))

    if abs(array[left] + array[right]) == 0:
        print('case1')
        min = abs(array[left] + array[right])
        min_left = left
        min_right = right
        break

    if abs(array[left] + array[right - 1]) < abs(array[left + 1] + array[right]) and (right - left) >= 2:
        print('case2')
        if abs(array[left] + array[right - 1]) < min:
            print('case2-1')
            min = abs(array[left] + array[right - 1])
            min_left = left
            min_right = right - 1
        right -= 1
    elif abs(array[left] + array[right - 1]) >= abs(array[left + 1] + array[right]) and (right - left) >= 2:
        print('case3')
        if abs(array[left + 1] + array[right]) < min:
            print('case3-1')
            min = abs(array[left + 1] + array[right])
            min_left = left + 1
            min_right = right
        left += 1
    else:
        print('case4')
        right -= 1
    

print(array[min_left], array[min_right])

