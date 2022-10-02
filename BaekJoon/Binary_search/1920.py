import sys

n = int(input())
a = set(map(int, sys.stdin.readline().split()))
m = int(input())
b = map(int, sys.stdin.readline().split())


### 이분 탐색을 활용한 풀이
# def binary(l, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if l == N[m]:
#         return 1
#     elif l < N[m]:
#         return binary(l, N, start, m-1)
#     else:
#         return binary(l, N, m+1, end)

# for i in b:
#     print(binary(i, a, 0, len(a) - 1))

for i in b:
    print(1) if i in a else print(0)
