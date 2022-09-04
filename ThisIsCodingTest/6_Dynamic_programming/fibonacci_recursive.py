import time

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input())

start_time = time.time()
print(fibo(n))
end_time = time.time()

print(end_time - start_time)
