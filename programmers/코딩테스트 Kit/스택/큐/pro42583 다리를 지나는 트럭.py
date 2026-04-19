from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque(list([0]*bridge_length))
    current_weight = 0
    while trucks or current_weight:
        current_weight -= bridge.popleft()
        if trucks and current_weight+trucks[0] <= weight:
            truck = trucks.popleft()
            current_weight += truck
            bridge.append(truck)
        else: bridge.append(0)
        answer += 1
    return answer

print(solution(100,100,[10]))