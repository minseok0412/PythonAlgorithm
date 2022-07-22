N, K = map(int, input().split())

list1 = [0] * N
list1 = list(input())
sum = 0
i = 0
j = 0
while i < len(list1):
    if list1[i] == "P":
        for k in range(K,0,-1):
            if i-k>= 0:
                if list1[i-k] == "H":
                    list1[i] = "M"
                    sum += 1
                    list1[i-k] = "R"
                    break
    i += 1

    if j < len(list1)-1:
        if list1[j] == "P":
            for k in range(K):
                if j+k+1 < len(list1):
                    if list1[j+k+1] == "H":
                        list1[j] = "M"
                        sum += 1
                        list1[j+k+1] = "R"
                        break
        j += 1
print(sum)