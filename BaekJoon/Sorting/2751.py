from random import randint

n = int(input())

# array = [int(input()) for i in range(n)]
array = [randint(0, 1000000) for i in range(n)]

array.sort()

for i in range(len(array)):
    print(array[i])
