def evaluate_polynomial(coefficients, x):
    result = 0
    power = 1
    for coefficient in coefficients:
        result += coefficient * power
        power *= x
    return result

def point_location(n, coefficients, x, y):
    y_poly = evaluate_polynomial(coefficients, x)
    if y < y_poly:
        return "Inside"
    elif y == y_poly:
        return "On"
    else:
        return "Outside"

while True:
    inputs = list(map(int, input().split()))
    n = inputs[0]
    if n == 0:
        break
    coefficients = inputs[1:]
    x, y = map(int, input().split())
    result = point_location(n, coefficients, x, y)
    print(result)
