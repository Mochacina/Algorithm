l=input()
n=len(l)
print("true" if list(l)[0:(n//2)+1:1] == list(l)[n:(n//2)-1:-1] else "false")