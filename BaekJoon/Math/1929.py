import time

M, N = map(int, input().split())

start_time = time.time()
N += 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False
for i in range(M, N):
    if i > 1:
        if sieve[i]:
            print(i)

end_time = time.time()
print(end_time - start_time)
