N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]
l = [0] * (d+1)
l[c] = 1
ate = 1

for i in range(k):
    sushi = sushis[i%N]
    if not l[sushi]: ate += 1
    l[sushi] += 1
    
max_n = ate

for i in range(N):
    out_sushi = sushis[i%N]
    in_sushi = sushis[(i+k) % N]

    l[out_sushi] -= 1
    if not l[in_sushi]: ate += 1
    if not l[out_sushi]: ate -= 1  
    l[in_sushi] += 1
    
    max_n = max(ate, max_n)

print(max_n)