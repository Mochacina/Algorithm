def draw_triangle(n):
    # 2D 배열(공백으로 채움)
    canvas = [[' ' for _ in range(2 * n - 1)] for _ in range(n)]
    
    def fill(x, y, size):
        if size == 3:
            # 기본 삼각형 패턴
            canvas[x][y] = '*'
            canvas[x + 1][y - 1] = '*'
            canvas[x + 1][y + 1] = '*'
            for i in range(-2, 3):
                canvas[x + 2][y + i] = '*'
        else:
            half = size // 2
            # 위쪽 삼각형
            fill(x, y, half)
            # 왼쪽 아래 삼각형
            fill(x + half, y - half, half)
            # 오른쪽 아래 삼각형
            fill(x + half, y + half, half)

    fill(0, n - 1, n)  # 시작점: 꼭대기, 가운데 정렬
    return [''.join(row) for row in canvas]

# 실행
n = int(input())
result = draw_triangle(n)
print('\n'.join(result))