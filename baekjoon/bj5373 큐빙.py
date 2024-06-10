from collections import deque

"""
      1 2 3
      4 5 6
      7 8 9
101112131415161718192021
222324252627282930313233
343536373839404142434445
      464748
      495051
      525354
"""

# 10~21
# 34~45
# 1 4 7 13 25 37 46 49 52 45 33 21
# 3 6 9 15 27 39 48 51 54 43 31 19
# 1 2 3 18 30 42 54 53 52 34 22 10
# 7 8 9 16 28 40 48 47 46 36 24 12

cube = "WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY"

for _ in range(int(input())):
    n = int(input())
    l = [*input().split()]
    for i in l:
        pass