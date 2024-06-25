def min_presses(N, target):
    # 초기 상태는 모두 0 (꺼진 상태)
    state = [0] * N
    
    # 목표 상태
    target = list(map(int, target.split()))
    
    press_count = 0
    for i in range(N):
        if state[i] != target[i]:
            press_count += 1
            # 현재 버튼과 오른쪽 두 버튼을 토글
            state[i] = 1 - state[i]
            if i + 1 < N: state[i + 1] ^= 1
            if i + 2 < N: state[i + 2] ^= 1
    
    return press_count

# 입력 받기
N = int(input())
target = input()

# 결과 출력
print(min_presses(N, target))