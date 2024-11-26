def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def approx_sin(x, n):
    res = 0
    for i in range(n+1):
        res += (-1) ** i * (x ** (2*i+1)) / factorial(2*i+1)
    return res


def approx_cos(x, n):
    res = 0
    for i in range(n+1):
        res += (-1) ** i * (x ** (2*i)) / factorial(2*i)
    return res


def approx_sinh(x, n):
    res = 0
    for i in range(n+1):
        res += x ** (2*i+1) / factorial(2*i+1)
    return res


def approx_cosh(x, n):
    res = 0
    for i in range(n+1):
        res += x ** (2*i) / factorial(2*i)
    return res


print(approx_sin(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))
