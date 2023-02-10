N = int(input())

num = list(map(int, input().split()))

result = []

for i in range(N,0,-1):
    if i == N:
        result.append(i)
        num.pop(-1)
    else:
        result.insert(num[-1], i)
        num.pop(-1)

for i in result:
    print(i,"",end="")