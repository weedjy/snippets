z = dict()

def fib(n):
    if n in z.keys():
        return z[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        q = fib(n-1)+fib(n-2)
        z[n] = q
        return q

def main():
    n = int(input())
    print(fib(n))

    
# fib in one line
# print(f'Fibonacci nums: {" ".join((lambda f, *args: f(f, *args))((lambda f, n, a, b: [str(b)] + f(f, n - 1, b, a + b) if n else []), 20, 0, 1))}')


if __name__ == "__main__":
    main()
