def fib(n):
    '''nより小さな数字でフィボナッチ数列を出す'''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
