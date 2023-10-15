def solution(food):
    answer = ""
    for i in range(1,len(food)):
        answer = answer + f"{i}"*(food[i]//2)
    answer = answer + "0" + answer[::-1]
    return answer

food = [1, 3, 4, 6]	
print("result:", solution(food))
