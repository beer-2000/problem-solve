from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and (not (nx == 0 and ny == 0)):
                print(f'{nx}, {ny} 지점에 1을 더합니다')
                graph[nx][ny] = graph[x][y] + 1
                for i in range(n):
                    for j in range(m):
                        print(graph[i][j], end='')
                    print()
                queue.append((nx, ny))
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
print()

for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()
