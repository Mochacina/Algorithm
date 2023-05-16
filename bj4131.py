# def primechk(n):
#     if(n in [0,1]): return False
#     for k in range(2,int(j**0.5)+1):
#         if (j%k==0): return False
#     return True
    
# for i in range(int(input())):
#     j=int(input())
#     while(True):
#         if primechk(j):print(j);break
#         j+=1
        
      
for _ in range(int(input())):
 m=1;n=int(input())
 if(n in[0,1]):n=3;m=0
 while m:
  m=0
  for i in range(2,int(n**0.5)+1):
   if (n%i==0):m=1;break
  n+=1
 print(n-1)