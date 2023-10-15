import sys

def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    
    # 배열 초기화
    arr = [[100000*200 for _ in range(n)] for _ in range(n)]
    for r in range(n): arr[r][r] = 0
    for sta, end, fee in fares:
        arr[sta-1][end-1], arr[end-1][sta-1] = fee, fee
    
    for k in range(n): # 경유지점 
        for i in range(n): # 지점 A
            for j in range(n): # 지점 B
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])
                
    # for i in arr: print(i)
    
    answer = 100000*200
    
    for i in range(n): answer = min(arr[i][s] + arr[i][a] + arr[i][b], answer)
    
    return answer

n = 6 # 총 노드 갯수
s = 4 # 시작지점
a = 6 # a 도착지점
b = 2 # b 도착지점

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(sys.maxsize)
print(solution(n,s,a,b,fares))