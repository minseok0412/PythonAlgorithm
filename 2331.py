A, P = map(int, input().split())

temp = []
final = [A]
sum = 0
sum1 = 0
sum2 = 0
y = 0
while y<500:
    result = list(map(int, str(A)))

    for i in range(len(result)):
        k = result[i]
        j = k ** P
        temp.append(j)

    for i in range(len(result)):
        sum += temp[i]

    temp.clear()
    final.append(sum)
    A = sum
    sum = 0
    y += 1

for m in range(len(final)):
    for n in range(len(final)):
        if m == n:
            n += 1
        else:
            if final[m] == final[n]:
                sum1 = 1
    if sum1 == 0:
        sum2 += 1
        sum1 = 0

print(sum2)