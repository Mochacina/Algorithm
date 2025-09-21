import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))

    # dp[i][j]는 i부터 j까지 합치는 최소 비용
    dp = [[sys.maxsize] * K for _ in range(K)]
    for i in range(K):dp[i][i] = 0
    
    # opt[i][j]는 dp[i][j]를 만드는 최적의 분할 지점 k
    opt = [[0] * K for _ in range(K)]

    # 누적 합 배열 (Prefix Sum)
    S = [0] * (K + 1)
    for i in range(K):
        S[i+1] = S[i] + files[i]
        opt[i][i] = i

    # length는 합치는 파일의 개수
    for length in range(2, K + 1):
        # i는 시작 파일의 인덱스
        for i in range(K - length + 1):
            j = i + length - 1

            # --- 헬레나 님의 크누스-야오 최적화 강의 ---
            # 일반적인 DP는 k를 i부터 j-1까지 모두 탐색해서 O(K^3)이 걸려. 하지만 그럴 필요 없지!
            #
            # [핵심] opt[i][j-1] <= opt[i][j] <= opt[i+1][j]
            # '더 큰 범위(i~j)의 최적 분할점(opt[i][j])은,
            #  그것보다 작은 범위(i~j-1)의 최적 분할점과 (i+1~j)의 최적 분할점 사이에 존재한다!'
            #
            # 이 마법의 부등식 덕분에 k의 탐색 범위가 엄청나게 줄어서 O(K^2)가 되는 거야!
            start_k = opt[i][j-1]
            end_k = opt[i+1][j]

            # k는 i와 j 사이의 분할점이므로, k는 j보다 작아야 한다! (Index Error 방지)
            for k in range(start_k, min(end_k, j - 1) + 1):
                current_cost = dp[i][k] + dp[k+1][j] + (S[j+1] - S[i])
                
                if dp[i][j] > current_cost:
                    dp[i][j] = current_cost
                    opt[i][j] = k

    print(dp[0][K-1])