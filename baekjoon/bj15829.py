L = int(input())
n = input()
print(sum([(ord(n[i])-96)*(31**i) for i in range(L)])%1234567891)