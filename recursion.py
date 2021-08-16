# n is the nth number in the Fibonacci sequence
def rFib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)