import sys

input = sys.stdin.readline
n = int(input())
if n == 1:exit(print(0))

matrices = [list(map(int,input().split())) for _ in range(n)]

dp = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):dp[i][i] = 0

# length는 곱하는 행렬의 개수 (2개부터 N개까지)
for length in range(2, n+1):
    for i in range(n-length+1): # i는 시작 행렬의 인덱스
        j = i + length - 1  # j는 끝 행렬의 인덱스
        
        # k는 i와 j 사이를 나누는 기준점
        # (i...k)와 (k+1...j) 두 그룹으로 나눔
        for k in range(i, j):
            # 점화식 적용! 꺄르륵, 수학 초보들을 위한 헬레나 님의 친절한 해설 시간!
            # cost = (i부터 k까지 곱하는 최소 비용) + (k+1부터 j까지 곱하는 최소 비용) + (두 결과 행렬을 마지막으로 곱하는 비용)
            #
            # 1. dp[i][k]: i부터 k까지의 행렬들을 이미 최적의 순서로 곱했을 때의 최소 비용. (이미 계산해뒀지!)
            # 2. dp[k+1][j]: k+1부터 j까지의 행렬들을 이미 최적의 순서로 곱했을 때의 최소 비용. (이것도!)
            # 3. matrices[i][0] * matrices[k][1] * matrices[j][1]:
            #    - (i~k)를 곱한 결과 행렬의 크기는 (i행렬의 행) x (k행렬의 열) = matrices[i][0] x matrices[k][1]
            #    - (k+1~j)를 곱한 결과 행렬의 크기는 (k+1행렬의 행) x (j행렬의 열) = matrices[k+1][0] x matrices[j][1]
            #    - 두 결과 행렬을 곱하는 비용은 (첫째 행렬의 행) * (첫째 행렬의 열) * (둘째 행렬의 열)
            #    - 즉, matrices[i][0] * matrices[k][1] * matrices[j][1] 가 된다!
            cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            
            # 더 작은 비용으로 갱신
            dp[i][j] = min(dp[i][j], cost)

# 최종 결과는 0번째부터 n-1번째 행렬까지 곱하는 최소 비용
print(dp[0][n-1])