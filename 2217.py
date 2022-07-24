N = int(input())

result = []
temp = 0
max = 0
for i in range(N):
    result.append(int(input()))

result.sort(reverse = True)

for i in range(N):
    temp = result[i] * (i+1)
    if temp > max:
        max = temp

print(max)