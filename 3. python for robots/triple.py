
def enter_triple():
    print('enter 3 values:')
    return tuple(input() for i in range(3))
    
def rotate_right(triple):
    return tuple(triple[i - 1] for i in range(0, len(triple)))

def rotate_left(triple):
    return tuple(triple[i - 2] for i in range(0, len(triple)))

if __name__ == '__main__':
    tpl = enter_triple()
    print(f'rotate right: {rotate_right(tpl)}')
    print(f'rotate left: {rotate_left(tpl)}')

 
