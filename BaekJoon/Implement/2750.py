N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))

numbers_set = set(numbers)
result = list(numbers_set)
result.sort()

for i in result:
  print(i)
