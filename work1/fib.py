def fib(x):
        return 0 if x == 0 else 1 if x == 1 else fib(x - 1) + fib(x - 2)

if __name__ == '__main__':
    print(f'fib = {fib(int(input("enter value for call fib() function: ")))}')
