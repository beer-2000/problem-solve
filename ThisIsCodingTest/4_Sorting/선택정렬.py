from random import randint
import time
start_time = time.time()

# list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

list = []
for _ in range(10000):
    list.append(randint(1, 100))
    
# list.sort(reverse=True)
memory = 0
for i in range(len(list)):
    for j in range(i+1, len(list)):
        # print('this round i, j:', i, j)
        # print('this round list value:', list[i], list[j])
        if list[i] > list[j]:
            # print('work')
            memory = list[i]
            list[i] = list[j]
            list[j] = memory
            # print(list)

print(list)
print("time : ", time.time() - start_time)
