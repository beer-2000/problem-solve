import time

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

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
