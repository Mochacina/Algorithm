import sys
import math
input = sys.stdin.readline

class SegTree():
    """
    이 세그먼트 트리는 각 구간의 '최소값의 인덱스'를 저장합니다.
    """
    def __init__(self, data) -> None:
        self.n = len(data)
        self.data = data
        # 트리 크기를 더 정확하게 계산해서 메모리를 절약!
        h = math.ceil(math.log2(self.n))
        self.tree = [0] * (1 << (h + 1))
        self.init(1, 0, self.n - 1)

    def init(self, node, start, end):
        # 리프 노드에는 해당 데이터의 인덱스를 저장
        if start == end:
            self.tree[node] = start
            return
        
        mid = (start + end) // 2
        self.init(2 * node, start, mid)
        self.init(2 * node + 1, mid + 1, end)
        
        # 두 자식 노드 중 더 작은 값을 가진 인덱스를 부모 노드에 저장
        # 값이 같으면 인덱스가 작은 쪽을 선택 (문제 조건)
        left_child_idx = self.tree[2 * node]
        right_child_idx = self.tree[2 * node + 1]
        
        if self.data[left_child_idx] <= self.data[right_child_idx]:
            self.tree[node] = left_child_idx
        else:
            self.tree[node] = right_child_idx

    def update(self, node, start, end, index):
        # 업데이트할 인덱스가 현재 노드 범위 밖이면 무시
        if not (start <= index <= end):
            return

        # 리프 노드에 도달하면 업데이트 종료 (실제 데이터 배열은 밖에서 바뀜)
        if start == end:
            return

        mid = (start + end) // 2
        self.update(2 * node, start, mid, index)
        self.update(2 * node + 1, mid + 1, end, index)

        # 자식 노드가 변경되었을 수 있으니, 현재 노드의 값(인덱스)을 다시 계산
        left_child_idx = self.tree[2 * node]
        right_child_idx = self.tree[2 * node + 1]

        if self.data[left_child_idx] <= self.data[right_child_idx]:
            self.tree[node] = left_child_idx
        else:
            self.tree[node] = right_child_idx

    def query(self, node, start, end, left, right):
        # 쿼리 범위가 현재 노드 범위를 완전히 벗어나면 -1 (유효하지 않은 인덱스) 반환
        if right < start or left > end:
            return -1
        
        # 쿼리 범위가 현재 노드 범위를 완전히 포함하면, 현재 노드에 저장된 인덱스 반환
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_res_idx = self.query(2 * node, start, mid, left, right)
        right_res_idx = self.query(2 * node + 1, mid + 1, end, left, right)

        # 한쪽 결과가 유효하지 않으면 다른 쪽 결과를 반환
        if left_res_idx == -1:
            return right_res_idx
        if right_res_idx == -1:
            return left_res_idx
        
        # 두 결과 모두 유효하면, 더 작은 값을 가진 인덱스를 반환
        if self.data[left_res_idx] <= self.data[right_res_idx]:
            return left_res_idx
        else:
            return right_res_idx

# --- 메인 로직 ---
n = int(input())
A = list(map(int, input().split()))

# 세그먼트 트리 생성
st = SegTree(A)
for _ in range(int(input())):
    query = list(map(int, input().split()))
    
    # 1번 쿼리: Ai를 v로 변경
    if query[0] == 1:
        A[query[1]-1] = query[2]  # 원본 데이터 배열 업데이트
        st.update(1, 0, n-1, query[1]-1)  # 세그먼트 트리 업데이트
    
    # 2번 쿼리: Ai부터 Aj까지 최소값의 인덱스 출력
    elif query[0] == 2:
        min_idx = st.query(1, 0, n-1, query[1]-1, query[2]-1)
        # 출력은 1부터 시작하는 인덱스로
        print(min_idx+1)
    
    del query