import sys

n = int(input())
numbers = sorted(list(range(1, n + 1)), reverse=True)
example = []
for i in range(n):
    example.append(int(sys.stdin.readline().rstrip()))

stack = []
result = []
plus_minus = []

for a in example:
    if numbers.count(a) == 1:
        index_numbers = numbers.index(a)
        temp = numbers[index_numbers:]
        temp.reverse()
        stack += temp
        del numbers[index_numbers:]
        plus_minus += ['+'] * len(temp)
        result.append(stack.pop())
        plus_minus.append('-')
        
    elif stack.count(a) == 1:
        index_stack = stack.index(a)
        if index_stack != len(stack) - 1:
            print("NO")
            plus_minus = []
            break
        result.append(stack.pop())
        plus_minus.append('-')
 
if len(plus_minus) != 0:
    for a in plus_minus:
        print(a)
