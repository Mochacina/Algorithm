import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

is_strict = 1
for i in range(N - 1):
    if A[i] >= A[i + 1]:
        is_strict = 0
        break

print(is_strict)