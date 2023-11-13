def c(n):
 if n==0:return '-'
 l=c(n-1)
 return l+" "*(3**(n-1))+l
while True:
 try:print(c(int(input())))
 except:break