def fibonacci(n):
    fibo = []
    a = 0
    b = 1
    while a <= n:
        fibo.append(a)
        print(a)
        a, b = b, a+b
    return fibo

print(fibonacci(100))