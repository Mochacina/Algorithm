from collections import deque

def hide_and_seek(N, K):
    MAX = 100000
    dist = [-1] * (MAX + 1)
    ways = [0] * (MAX + 1)

    q = deque()
    q.append(N)
    dist[N] = 0
    ways[N] = 1

    while q:
        now = q.popleft()
        for nxt in (now - 1, now + 1, now * 2):
            if 0 <= nxt <= MAX:
                if dist[nxt] == -1:
                    dist[nxt] = dist[now] + 1
                    ways[nxt] = ways[now]
                    q.append(nxt)
                elif dist[nxt] == dist[now] + 1:
                    ways[nxt] += ways[now]

    return dist[K], ways[K]


# 실행 예시
N, K = map(int, input().split())
time, count = hide_and_seek(N, K)
print(time)
print(count)