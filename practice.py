# import sys
array = [list(map(int, input().split())) for _ in range(10)]
# array = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]


x = 2
y = 2

while True:
    if array[x - 1][y - 1] == 2:
        array[x - 1][y - 1] = 9
        break

    if array[x - 1][y - 1] == 0:
        array[x - 1][y - 1] = 9

    if array[x - 1][y] != 1:
        y += 1
        continue
    
    if array[x][y - 1] != 1:
        x += 1
        continue

    break
    
    
        
# print('---------')
for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()
