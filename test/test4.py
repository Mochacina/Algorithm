import timeit

# 전역 변수를 사용하는 버전
x = 0
def global_increment():
    global x
    for _ in range(multi):
        x += 1

# 지역 변수를 사용하는 버전
def local_increment():
    x = 0
    for _ in range(multi):
        x += 1

multi = int(input("input: "))

# 성능 측정
global_time = timeit.timeit(global_increment, number=1)
local_time = timeit.timeit(local_increment, number=1)

print(f"Global variable time: {global_time:.6f} seconds")
print(f"Local variable time: {local_time:.6f} seconds")
print(f"Local is {global_time/local_time:.2f}x faster")