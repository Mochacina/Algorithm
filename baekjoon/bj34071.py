l = [int(input())for _ in range(int(input()))]
print("ez" if l[0]==min(l) else "hard" if l[0]==max(l) else "?")