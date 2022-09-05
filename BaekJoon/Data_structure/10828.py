import sys

n = int(sys.stdin.readline().rstrip())

stack = []

for i in range(n):
    command = str(sys.stdin.readline().rstrip())
    if command.find('push') != -1:
        number = int(command.split()[1])
        stack.append(number)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(int(len(stack) == 0))
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
