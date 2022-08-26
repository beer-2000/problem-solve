N = int(input())

five = N // 5 + 1
three = N // 3 + 1
result = 0
end_point = False

# print('five: ', five)
# print('three: ', three)

for i in range(five + 1):
  if end_point == True:
    break
  for j in range(three):
    # print('five - i: ', five-i)
    # print('j: ', j)
    # print('N: ', N)
    # print(((five-i) * 5) + (j * 3))
    if N == (((five-i) * 5) + (j * 3)):
      result = (five - i) + j
      end_point = True
      break

if result == 0:
  result = -1
  
print(result)
