for _ in range(int(input())):
    l = list(input().split())
    for i, args in enumerate(l): l[i] = args[::-1]
    print(' '.join(l))
