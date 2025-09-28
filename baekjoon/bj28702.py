l = [input() for _ in range(3)]
num = 0
for i,n in enumerate(l):
    if n.isdigit():
        num = int(n)+3-i
        break
if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0:
    print('Fizz')
elif num%5==0:
    print('Buzz')
else:print(num)