
def diff(a, b):
    diff = a - b
    return abs((diff + 180) % 360 - 180)

if __name__ == '__main__':
    a = int(input('enter 1st corner: '))
    b = int(input('enter 2d corner: '))
    print(f'{diff(a,b)}')