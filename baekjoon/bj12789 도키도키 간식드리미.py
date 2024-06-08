N = int(input())
students = [*map(int, input().split())]
stack = []
cnt = 1

for student in students:
    stack.append(student)
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt +=1

print('Sad' if stack else 'Nice') 