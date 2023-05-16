# a = int(input())
# distance = list(map(int,input().split()))
# price = list(map(int,input().split()))
# total = 0

# p = len(distance)
# del price[len(price)-1]
# while(p):
#     n = price.index(min(price))
#     total += sum(distance[n:])*price[n]
#     del distance[n:]
#     del price[n:]
#     p -= (p-n)
# print(total)

a = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
_min = price[0]
total = 0
for i in range(a-1):
    _min = min(_min,price[i])
    total += distance[i]*_min
print(total)