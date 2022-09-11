start_time = time.time()
def check_prime(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                return False
        return True

n, m = map(int, input().split())

for i in range(n, m + 1):
    if check_prime(i) == True:
        print(i)
end_time = time.time()

print(end_time - start_time)
