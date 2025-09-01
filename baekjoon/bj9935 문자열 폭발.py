import sys

input = sys.stdin.readline
string = input().rstrip()
bomb = input().rstrip()
stack = []
bomb_len = len(bomb)

for ch in string:
    stack.append(ch)
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

result = ''.join(stack)
print(result if result else "FRULA")
