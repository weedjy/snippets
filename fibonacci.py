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


if __name__ == "__main__":
    main()
