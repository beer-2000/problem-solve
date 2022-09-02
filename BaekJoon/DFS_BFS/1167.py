import sys
sys.setrecursionlimit(10000)

t = int(input())
result_list = [0 for i in range(t)]

def dfs(x, y):
    # print('x, y in dfs :', x, y)
    if x < 0 or x >= m or y < 0 or y >=n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for p in range(t):
    m, n, k = map(int,sys.stdin.readline().split())
    graph = [[0 for x in range(m)] for y in range(n)]

    for _ in range(k):
        x, y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result_list[p] += 1


for i in range(t):
    print(result_list[i])
