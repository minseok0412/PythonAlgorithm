N, M = map(int, input().split())

word1 = []
word2 = []
result1 = []

for i in range(N):
    word1.append(input())

for i in range(M):
    word2.append(input())

word1 = set(word1)
word2 = set(word2)

result1 = sorted(word1 & word2)


print(len(result1))
for i in result1:
    print(i)