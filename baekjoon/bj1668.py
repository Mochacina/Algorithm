N = int(input())
l = [int(input()) for _ in range(N)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for n in l:
    if n > left_max:
        left_max = n
        left_cnt += 1
for n in l[::-1]:
    if n > right_max:
        right_max = n
        right_cnt += 1
print(f"{left_cnt}\n{right_cnt}")