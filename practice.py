import time

# n, m = map(int, input().split())

# start_time = time.time()
# numbers = [2]

# for i in range(3, m + 1):
#     cnt = 0
#     for number in numbers:
#         if i % number == 0:
#             cnt += 1
#             break
#     if cnt == 0:
#         numbers.append(i)

# cnt = 0
# for i in range(n, m + 1):
#     if i in numbers:
#         print(i)
# end_time = time.time()
# print(end_time - start_time)



# --------------------------------

# n, m = map(int, input().split())

# # start_time = time.time()
# array = list(range(2, m + 1))
# array = [2] + [i for i in array if i % 2 == 1]

# index = 0
# while True:
#     array = array[0:index + 1] + [i for i in array[index + 1:] if i % array[index] != 0]
#     index += 1
#     if index >= len(array):
#         break
#     if array[index] >= m ** 0.5 + 1:
#         break

# result = [i for i in array if n <= i]
# for number in result:
#     print(number)

# end_time = time.time()
# print(end_time - start_time)


# ---------------------------------

# start_time = time.time()
# def check_prime(number):
#     if number == 1:
#         return False
#     else:
#         for i in range(2, int(number ** 0.5 + 1)):
#             if number % i == 0:
#                 return False
#         return True

# n, m = map(int, input().split())

# for i in range(n, m + 1):
#     if check_prime(i) == True:
#         print(i)
# end_time = time.time()

# print(end_time - start_time)


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


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
