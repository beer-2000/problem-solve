from collections import deque

n, m = map(int, input().split())
result = 0
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(r, c):
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()

        if r < 0 or r >= n or c < 0 or c >= m:
            continue

        if visited[r][c] == 1:
            continue

        if graph[r][c] == '-':
            visited[r][c] = 1
            if c - 1 >= 0:
                if graph[r][c - 1] == '-':
                    queue.append((r, c - 1))
            if c + 1 < m:
                if graph[r][c + 1] == '-':
                    queue.append((r, c + 1))

        if graph[r][c] == '|':
            visited[r][c] = 1
            if r - 1 >= 0:
                if graph[r - 1][c] == '|':
                    queue.append((r - 1, c))
            if r + 1 < n:
                if graph[r + 1][c] == '|':
                    queue.append((r + 1, c))
            

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)
