import sys
sys.setrecursionlimit(10**5)

preorder = list(map(int, sys.stdin.read().split()))

def solve(pre, mn, mx):
    if not pre or pre[0] < mn or pre[0] > mx:
        return []
    root = pre.pop(0)
    left = solve(pre, mn, root)
    right = solve(pre, root, mx)
    return left + right + [root]

result = solve(preorder[:], -float('inf'), float('inf'))
for x in result:print(x)