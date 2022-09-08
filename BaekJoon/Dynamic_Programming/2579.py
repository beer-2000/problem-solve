n = int(input())

array = [0] * (n + 3)
for i in range(n):
    array[i + 1] = int(input())

dp = [0] * (n + 3)
dp[1] = array[1]
dp[2] = array[1] + array[2]
dp[3] = max(dp[1] + array[3], dp[2] + array[3])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + array[i - 1] + array[i], dp[i - 2] + array[i])

print(dp[n])
