N, M = map(int, input().split())
l = list(map(int, input().split()))
l2 = [0]*(N+1)
for i in range(1, N+1):
    l2[i] = l2[i-1]+l[i-1]
    
cnt = 0 
for i in range(1, N+1):
    for j in range(i, N+1):
        if l2[j]-l2[i-1] == M:
            cnt += 1

print(cnt)

# 01. l2[i] = l2[i-1]+l[i-1] is a prefix sum array.
# It is used to calculate the sum of elements in a range in O(1) time.