for i in range(int(input())):
    k = int(input())

    word = []

    a = list(input().split())

    word.append(a[0])
    a.pop(0)

    for i in a:
        if i <= word[0]:
            word.insert(0, i)
        else:
            word.append(i)

    print("".join(word))