import sys

n = int(input())
array = sorted(list(map(int, sys.stdin.readline().split())))
x = int(input())

count = 0
left, right = 0, n-1

while left < right:
    sum = array[left] + array[right]
    if sum == x:
        count += 1
        left += 1
    elif sum > x:
        right -= 1
    elif sum < x:
        left += 1
    
print(count)


# import sys

# n = int(input())
# array = sorted(list(map(int, sys.stdin.readline().split())))
# x = int(input())

# count = 0

# for i in range(len(array)):
#     for j in range(i, len(array)):
#         if array[i] >= (x//2 + 1):
#             break
#         if array[i] + array[j] == x:
#             count += 1
	
# print(count)
