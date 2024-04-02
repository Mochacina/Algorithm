# 가장 인접한 번호로 이동 후 +, - 버튼을 누르는 횟수를 최소화하는 문제
# 브루트 포스를 활용한 기존 풀이 방법
N = int(input())
M = int(input())
broken = []
ans = abs(N - 100)
try:
    broken = list(map(int, input().split()))
except:
    pass
for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in broken:
            break
    else:
        ans = min(ans, abs(N - i) + len(str(i)))
print(ans)

# 내가 생각하는 풀이 방법
# +,- 만을 이용해 이동하는 최악의 해를 구한다.
# 만약 고장나지 않은 버튼만으로 이동할 수 있다면 그것이 최선의 해이다.
# 만약 고장나지 않은 버튼만으로 이동할 수 없다면,
# 고장나지 않은 버튼을 이용해 N과 가장 가까운 수를 구하고
# # 그 수와 N의 차이에 +,- 버튼을 누르는 횟수를 더한 값과 최악의 해를 비교한다.
# N = int(input())
# M = int(input())
# broken = []
# ans = abs(N - 100)
# try:broken = list(map(int, input().split()))
# except:pass
# num = ''
# for n, i in enumerate(str(N)):
#     if int(i) in broken:
#         unbroken = [i for i in range(10) if i not in broken]
#         # i보다 작은 수 중 가장 큰 수
#         try:
#             a = max([j for j in unbroken if j < int(i)])
#             under = int(num + str(a) + str(max(unbroken))*len(str(N)[n+1:]))
#         except:under = int(num + str(max(unbroken))*len(str(N)[n+1:]))
#         # i보다 큰 수 중 가장 작은 수
#         try:
#             b = min([j for j in unbroken if j > int(i)])
#             upper = int(num + str(b) + str(min(unbroken))*len(str(N)[n+1:]))
#         except:upper = int(str(min(unbroken))*(len(str(N))+1))
#         print(min(ans, abs(N - under) + len(str(under)), abs(N - upper) + len(str(upper))))
#         break
#     else: num += i
# else:
#     print(min(ans, len(str(N))))
