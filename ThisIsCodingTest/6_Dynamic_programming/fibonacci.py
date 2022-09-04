# 시간복잡도 O(n)
import time
memory = [1, 1]

def fibo(n):
    if len(memory) >= n:
        return memory[n-1]
    for i in range(len(memory), n):
        memory.append(memory[i-1] + memory[i-2])
    return memory[n-1]

n1 = int(input())
start_time = time.time()
print(fibo(n1))
end_time = time.time()
print(end_time - start_time)

n2 = int(input())
start_time = time.time()
print(fibo(n2))
end_time = time.time()
print(end_time - start_time)

n3 = int(input())
start_time = time.time()
print(fibo(n3))
end_time = time.time()
print(end_time - start_time)
