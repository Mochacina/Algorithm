import re
while(True):
    n = input()
    if n == '.':exit()
    a = re.sub('[A-Za-z ]',"",n)
    for _ in range(len(a)//2):
        a = re.sub('\(\)|\[\]',"",a)
    print('yes' if a =='.' else 'no')