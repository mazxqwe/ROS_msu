
if __name__ == '__main__':
    a = int(input('enter 1st number: '))
    b = int(input('enter 2d number: '))
    c = int(input('enter 3d number: '))
    print(f'{max(a,c) if a > b else max(b,c)}')
