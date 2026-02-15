l = []
for _ in range(int(input())):l.append(int(input()))
print("ez" if l[0]==min(l) else "hard" if l[0]==max(l) else "?")