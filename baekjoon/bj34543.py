n=int(input())
w=int(input())
s = n*10+(20 if n>=3 else 0)+(50 if n>=5 else 0)-(15 if w > 1000 else 0)
print(s if s>=0 else 0)