def solution(park, routes):
    position = {'N':[0,-1],'S':[0,1],'W':[-1,0],'E':[1,0]}
    
    x,y = 0,0
    for b,i in enumerate(park):
        if x+y:break
        for a,j in enumerate(i):
            if j=="S":x,y=a,b;break
    
    rt = routes[::-1]
    
    while rt:
        node = rt.pop()
        pos, dis = node.split()
        dis = int(dis)
        nx, ny = position[pos]
        x2, y2 = x,y
        chk = 1
        for _ in range(dis):
            x2,y2 = x2+nx,y2+ny
            if 0 > x2 or x2 >= len(park[0]) or 0 > y2 or y2 >= len(park) or park[y2][x2] == "X":
                chk=0;break
        
        if chk: x,y = x2,y2
    answer = [y,x]
    return answer

park = ["SOO","OXX","OOO"]	
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))