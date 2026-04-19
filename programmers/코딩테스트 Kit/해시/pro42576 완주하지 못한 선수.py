def solution(participant, completion):
    part={}
    for p in participant:
        part[p]=part.get(p,0)+1
    for c in completion:
        part[c]=part[c]-1
    for arg in part:
        if part[arg] != 0:
            return arg
    
solution(["leo", "kiki", "eden"],["eden", "kiki"])