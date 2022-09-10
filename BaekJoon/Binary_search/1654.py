import sys

k, n = map(int, input().split())
sticks = []
for i in range(k):
    sticks.append(int(sys.stdin.readline().rstrip()))


def count_sticks(sticks, length):
    count = 0
    for stick in sticks:
        count += stick // length
    return count

start = 0
end = sum(sticks) // n + 1

result = 0

while start <= end:
    mid = (start + end) // 2
    count = count_sticks(sticks, mid)
    if count < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
