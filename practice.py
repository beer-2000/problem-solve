k, n = map(int, input().split())
sticks = []
for i in range(k):
    sticks.append(int(input()))

length = sum(sticks) // n + 1
count = 0
while count < n:
    count = 0
    for stick in sticks:
        count += stick // length
    length -= 1

print(count)
print(length + 1)
