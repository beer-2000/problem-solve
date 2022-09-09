def count_chess(array):
    count_start_black = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and array[i][j] != 'B':
                count_start_black += 1
            if (i + j) % 2 == 1 and array[i][j] != 'W':
                count_start_black += 1

    count_start_white = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and array[i][j] != 'W':
                count_start_white += 1
            if (i + j) % 2 == 1 and array[i][j] != 'B':
                count_start_white += 1

    if count_start_white > count_start_black:
        return count_start_black
    else:
        return count_start_white

m, n = map(int, input().split())
array = [input() for _ in range(m)]

min = 2500

for i in range(m - 7):
    for j in range(n -7):
        array_slice = []
        for k in range(8):
            array_slice.append(array[i + k][j:j+8])
        temp = count_chess(array_slice)
        if min > temp:
            min = temp

print(min)
        