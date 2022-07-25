import sys
input = sys.stdin.readline

N, M = map(int, input().split())

number = list(map(int, input().split()))

sum = 0
result = [0]

for i in number:
    sum += i
    result.append(sum)

for i in range(M):
    a,b = map(int, input().split())
    print(result[b]-result[a-1])