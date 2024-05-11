n=input()
print(int(''.join(map(str, sorted([*map(int, input().split())],key=lambda x:str(x)*10,reverse=True)))))