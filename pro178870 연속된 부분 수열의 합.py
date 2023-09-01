# def solution(sequence, k):
#     if k in sequence:
#         i = sequence.index(k)
#         return [i,i]
    
#     e = 0
#     l = len(sequence)
#     prefsum = [0]*(l+1)
#     for i in range(l):
#         prefsum[i+1] = e+sequence[i]
#         e += sequence[i]
    
#     for i in range(1,l+1):
#         for j in range(i,l+1):
#             if prefsum[j]-prefsum[j-i]==k: return [j-i,j-1]
#             if prefsum[j]-prefsum[j-i]>k: break

# def solution(sequence, k):
#     e = 0
#     l = len(sequence)
    
#     for i in range(l):
#         for j in range(i,l): 
#             if sum(sequence[j-i:j+1])==k: return [j-i,j]
#             if sum(sequence[j-i:j+1])>k: break

# def solution(sequence, k):
#     if k in sequence:
#         i = sequence.index(k)
#         return [i,i]
    
#     e = 0
#     l = len(sequence)
#     prefsum = [0]*(l+1)
#     for i in range(l):
#         prefsum[i+1] = e+sequence[i]
#         e += sequence[i]
    
#     for i in range(1,l+1):
#         for j in range(i,l+1):
#             if prefsum[j]-prefsum[j-i]==k: return [j-i,j-1]
#             if prefsum[j]-prefsum[j-i]>k: break

def solution(sequence, k):
    r = 0
    sum = sequence[0]
    answer = []
    
    for l, left in enumerate(sequence):
        while sum < k and r < len(sequence)-1:
            r += 1
            sum += sequence[r]
        if sum == k: answer.append([l,r])
        print("l, r:",l,r)
        print("sum:", sum)
        sum -= left
        
        
    answer.sort(key=lambda x:x[1]-x[0])
    print(answer)
    return answer[0]

sequence = [1, 1, 1, 2, 3, 4, 5]	
k = 5
print(solution(sequence, k))