import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

class TrieNode:
    """
    트라이의 노드를 나타내는 클래스.
    자식 노드들을 딕셔너리 형태로 저장한다.
    """
    def __init__(self):
        # 자식 노드들을 저장할 딕셔너리
        # key: 먹이 이름 (str), value: TrieNode
        self.children = {}

class Trie:
    """
    트라이 자료구조 클래스.
    """
    def __init__(self):
        # 루트 노드는 비어있는 TrieNode
        self.root = TrieNode()

    def insert(self, path):
        """
        주어진 경로(먹이 리스트)를 트라이에 삽입한다.
        """
        # 루트에서부터 탐색 시작
        current_node = self.root
        
        # 경로의 각 먹이에 대해 반복
        for food in path:
            # 현재 노드의 자식 중에 해당 먹이가 없으면 새로 노드를 생성
            if food not in current_node.children:
                current_node.children[food] = TrieNode()
            # 다음 노드로 이동
            current_node = current_node.children[food]

def print_trie(node, depth=0):
    """
    트라이 구조를 재귀적으로 출력하는 함수.
    깊이 우선 탐색(DFS)을 사용한다.
    """
    # 현재 노드의 자식들을 사전 순으로 정렬
    sorted_children_keys = sorted(node.children.keys())
    
    # 정렬된 자식들에 대해 반복
    for key in sorted_children_keys:
        # "--" 접두사와 함께 먹이 이름 출력
        print("--" * depth + key)
        # 자식 노드에 대해 재귀 호출 (깊이 + 1)
        print_trie(node.children[key], depth + 1)

# 정보의 개수 N 입력
N = int(input())

# 트라이 객체 생성
trie = Trie()

# N개의 정보에 대해 반복
for _ in range(N):
    # 한 줄을 읽어 공백으로 분리
    line = input().split()
    # 첫 번째 요소는 먹이 정보의 개수 K, 나머지는 먹이 경로
    path = line[1:]
    # 경로를 트라이에 삽입
    trie.insert(path)
    
# 완성된 트라이 구조 출력
print_trie(trie.root)

# import sys
# input = sys.stdin.readline

# class TrieNode:
#     def __init__(self):
#         # key: 먹이 이름 (str), value: TrieNode
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, path):
#         current_node = self.root
        
#         for food in path:
#             if food not in current_node.children:
#                 current_node.children[food] = TrieNode()
#             current_node = current_node.children[food]

# def print_trie(node, depth=0):
#     sorted_children_keys = sorted(node.children.keys())
    
#     for key in sorted_children_keys:
#         print("--" * depth + key)
#         print_trie(node.children[key], depth + 1)

# N = int(input())
# trie = Trie()

# for _ in range(N):
#     line = input().split()
#     path = line[1:]
#     trie.insert(path)
    
# print_trie(trie.root)