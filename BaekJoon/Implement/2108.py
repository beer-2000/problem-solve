import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

array.sort()

s = sum(array)
max_number = max(array)
min_number = min(array)
length_array = len(array)

# 최빈값 구하는 로직
counter = Counter(array)
mode = counter.most_common() # 숫자:빈도 를 나타내는 튜플을 빈도 순으로 나열
mode = [i for i in mode if i[1] == mode[0][1]] # 빈도수가 최빈값과 같은 튜플들만 남긴다
mode_result = []

# 빈도가 아닌 숫자만 남긴다
for i in mode:
    mode_result.append(i[0])

mode_result.sort() # 정렬

# 최빈값이 2개 이상이면 2번째로 작은 수를, 아니면 최빈값을 저장한다.
if len(mode_result) >= 2:        
    mode_number = mode_result[1]
else:
    mode_number = mode_result[0]

# 출력
print(round(s / n))
print(array[length_array // 2])
print(mode_number)
print(max_number - min_number)

