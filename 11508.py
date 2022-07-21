N = int(input())

temp = []
result = []
sum = 0

for i in range(N):
    temp.append(int(input()))

k = len(temp)
temp.sort(reverse=True)

for i in range(N):
    if i % 3 != 2:
        sum += temp[i]

print(sum)