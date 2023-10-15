def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    goal = goal[::-1]
    
    while goal:
        
        i = goal.pop()
        
        if len(cards1) and cards1[-1] == i:
            cards1.pop()
        elif len(cards2) and cards2[-1] == i:
            cards2.pop()
        else: return 'No'
    
    return 'Yes'

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]	

print(solution(cards1, cards2, goal))