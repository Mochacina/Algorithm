import sys

# Yes! I am the one and only Helena!
# This is not code. This is ART.

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    opinions = sorted(int(sys.stdin.readline()) for _ in range(n))
    exclude_num = int(n * 0.15 + 0.5)
    
    # 핵심 로직: 제외할 의견이 있다면 슬라이싱, 없다면 전체 리스트 사용
    if exclude_num > 0:
        trimmed_opinions = opinions[exclude_num:-exclude_num]
    else:
        trimmed_opinions = opinions
    
    # 최종 평균 계산 및 출력
    # trimmed_opinions가 비어있을 수 있는 극단적인 경우를 대비
    if not trimmed_opinions:
        print(0)
    else:
        average = sum(trimmed_opinions) / len(trimmed_opinions)
        print(int(average + 0.5))
        
# n,*d=map(int,open(0))
# u=(n*3+10)//20
# print(int(sum(sorted(d)[u:n-u])/(n-u*2 or 1)+.5))