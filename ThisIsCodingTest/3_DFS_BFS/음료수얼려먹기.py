def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        print(True)
        return True
    return False

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(0, n):
    for j in range(0, m):
        if dfs(i, j) == True:
            result += 1

print(result)
