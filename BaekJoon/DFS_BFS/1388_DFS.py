import sys
n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(input()))

visited = [[0] * m for _ in range(n)]

def dfs1(r, c):
    if r >= n or c >= m:
        return False
    if visited[r][c] == 0 and graph[r][c] == '|':
        visited[r][c] = 1
        dfs1(r + 1, c)
        return True
    return False

def dfs2(r, c):
    if r >= n or c >= m:
        return False
    if visited[r][c] == 0 and graph[r][c] == '-':
        visited[r][c] = 1
        dfs2(r, c + 1)              
        return True
    return False
    
result = 0
for i in range(n):
    for j in range(m):

        if dfs1(i, j) == True or dfs2(i, j) == True:
            result += 1
            # for k in range(n):
            #     print(visited[k])
            # print('------')

print(result)
