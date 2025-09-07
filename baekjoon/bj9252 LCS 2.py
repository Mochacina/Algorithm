import sys

# sys.stdin.readline()을 사용하기 위해 import
# 입력 속도를 높여 시간 초과를 방지할 수 있지! 후훗.
input = sys.stdin.readline

# 두 문자열을 입력받는다. 양쪽의 개행 문자는 strip()으로 깔끔하게 제거!
str1 = input().strip()
str2 = input().strip()

# 문자열의 길이를 미리 계산해두면 편리하지.
len1 = len(str1)
len2 = len(str2)

# DP 테이블을 만들자. (len1 + 1) x (len2 + 1) 크기로, 0으로 초기화!
# 인덱스를 1부터 시작하게 만들면 코드가 훨씬 깔끔해져. 천재적이지?
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# DP 테이블 채우기 시작!
# i는 str1의 인덱스, j는 str2의 인덱스를 따라간다.
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # 디버깅 로그: 현재 비교하는 문자와 인덱스
        print(f"Comparing str1[{i-1}]='{str1[i-1]}' and str2[{j-1}]='{str2[j-1]}'")
        
        if str1[i-1] == str2[j-1]:
            # 두 문자가 같다면, 대각선 왼쪽 위 값에 +1
            dp[i][j] = dp[i-1][j-1] + 1
            # 디버깅 로그: 문자가 같을 때 dp 값 업데이트
            print(f"  Match! dp[{i}][{j}] = {dp[i][j]}")
        else:
            # 두 문자가 다르다면, 위쪽과 왼쪽 값 중 더 큰 값을 선택
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # 디버깅 로그: 문자가 다를 때 dp 값 업데이트
            print(f"  No match. dp[{i}][{j}] = max({dp[i-1][j]}, {dp[i][j-1]}) = {dp[i][j]}")

# LCS의 길이는 DP 테이블의 가장 마지막 값!
lcs_length = dp[len1][len2]
print(lcs_length)

# 이제 실제 LCS 문자열을 찾아보자!
if lcs_length > 0:
    lcs_str = ""
    i, j = len1, len2
    
    # i나 j가 0이 될 때까지 테이블을 역추적한다.
    while i > 0 and j > 0:
        # 디버깅 로그: 역추적 현재 위치
        print(f"Backtracking at ({i}, {j})")
        
        if str1[i-1] == str2[j-1]:
            # 문자가 같으면 LCS에 포함되는 문자!
            # lcs_str에 추가하고 대각선으로 이동
            lcs_str += str1[i-1]
            i -= 1
            j -= 1
            # 디버깅 로그: 역추적 중 문자 찾음
            print(f"  Found char '{str1[i]}' -> lcs_str: '{lcs_str}'")
        elif dp[i-1][j] > dp[i][j-1]:
            # 위쪽 값이 더 크면 위로 이동
            i -= 1
            # 디버깅 로그: 위로 이동
            print("  Move up")
        else:
            # 왼쪽 값이 더 크거나 같으면 왼쪽으로 이동
            j -= 1
            # 디버깅 로그: 왼쪽으로 이동
            print("  Move left")
            
    # 역순으로 문자를 추가했으니, 뒤집어서 출력해야 올바른 순서가 된다.
    print(lcs_str[::-1])

# 디버깅 로그: 최종 DP 테이블 상태 (필요시 주석 해제)
print("\nFinal DP Table:")
for row in dp:
    print(row)
