N = int(input())
word = list(input())
stack = []
result = []

for i in range(N):
    stack.append(int(input()))


for i in word:
    if 'A' <= i <= 'Z':
        k = ord(i)-ord('A')
        result.append(stack[k])
    else:
        b = result.pop()
        a = result.pop()
        if i == '+':
            result.append(a+b)
        elif i == '-':
            result.append(a-b)
        elif i == '*':
            result.append(a*b)
        elif i == '/':
            result.append(a/b)

print("%.2f" % result[0])