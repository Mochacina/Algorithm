def stairs_number(n):
    if n == 1:
        return [i for i in range(1, 10)]
    res = []
    for num in stairs_number(n - 1):
        last_digit = num % 10
        if last_digit > 0:
            res.append(num * 10 + last_digit - 1)
        if last_digit < 9:
            res.append(num * 10 + last_digit + 1)
    return res

def count_stairs(n):
    return len(stairs_number(n))

def main():
    n = int(input().strip())
    print(count_stairs(n) % 1000000000)

if __name__ == '__main__':
    main()