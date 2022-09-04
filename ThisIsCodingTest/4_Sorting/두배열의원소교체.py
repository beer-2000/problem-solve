import time

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

start_time = time.time()

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        print('break!!')
        break

print(a, b)
print(sum(a))

end_time = time.time()
print('time : ', end_time - start_time)
