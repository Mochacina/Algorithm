def solution(wallpaper):
    minX, maxX, minY, maxY = 50,0,50,0
    
    for y, i in enumerate(wallpaper):
        for x, j in enumerate(i):
            if j == '#':
                minX = min(x,minX)
                minY = min(y,minY)
                maxX = max(x,maxX)
                maxY = max(y,maxY)
    
    answer = [minY, minX, maxY+1, maxX+1]
    return answer

wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]

print(solution(wallpaper))