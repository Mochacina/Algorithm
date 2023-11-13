# n = int(input())
# sum = 0
# for i in range(1,n-1):
#     for j in range(i+1,n):
#         for k in range(j+1,n+1):
#             print(i,j,k)
#             sum+=1
# print(sum)

n = int(input())
s=0;sum = 0
for i in range(1,n-1):
    s+=i
    sum+=s
print(f"{sum}\n3")


#1 3 6 10 15 21 