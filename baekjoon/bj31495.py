s = input()
if len(s) >= 2 and s[0] == '"' and s[-1] == '"' and len(s[1:-1]) > 0:
    print(s[1:-1])
else:print("CE")
