import sys

n = int(input())
a = set(map(int, sys.stdin.readline().split()))
m = int(input())
b = map(int, sys.stdin.readline().split())


for i in b:
    print(1) if i in a else print(0)
