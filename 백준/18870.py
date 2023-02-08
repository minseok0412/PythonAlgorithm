N = int(input())
K = list(map(int,input().split()))
X = sorted(K)

dict = {}
start = 0
dict[X[0]] = 0
num = []

for i in range(len(X)-1):
    if X[i+1] == X[i]:
        dict[X[i+1]] = start
    else:
        start += 1
        dict[X[i+1]] = start

for i in range(len(X)):
    num.append(dict[K[i]])

for i in num:
    print(i,"",end='')

