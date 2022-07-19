N = input()

a = int(len(N))
M = int(N)
sum = 0
b = 0
i = 1
while True:
    if M <= 9:
        sum = M
        break
    else:
        if i == 1:
            b = (M - 10 ** (a-1) + 1) * a
            sum += b
            a -= 1
            i += 1
            if a == 0:
                break
        else:
            b = a * 9 * 10 ** (a-1)
            sum += b
            a -= 1
            if a == 0:
                break

print(sum)