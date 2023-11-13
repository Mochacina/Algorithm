def solution(players, callings):
    ranking = {player:i for i, player in enumerate(players)}
    for i in callings:
        rank = ranking[i]
        ranking[i] -= 1
        ranking[players[rank-1]] += 1
        players[rank], players[rank-1] = players[rank-1], i
    return players

p = list(input().split())
c = list(input().split())
print(p)
print(c)
print(solution(p,c))