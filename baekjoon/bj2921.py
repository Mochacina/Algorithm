n = int(input())
print(sum([sum([i+j for j in range(i, n + 1)]) for i in range(0, n + 1)]))