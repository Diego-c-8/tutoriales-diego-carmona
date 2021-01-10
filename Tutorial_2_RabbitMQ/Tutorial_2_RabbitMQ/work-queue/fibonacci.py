def get_fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return get_fib(n-1) + get_fib(n-2)