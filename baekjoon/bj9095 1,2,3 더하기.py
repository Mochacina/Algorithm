sum=0
def sol(s):
    global sum
    if s==0:sum+=1;return
    for i in range(1,min(4,s+1)):sol(s-i)
        
for _ in range(int(input())):
    sum=0
    sol(int(input()))
    print(sum)