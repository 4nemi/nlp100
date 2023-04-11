def gen_sentence(x, y, z):
    return  f'{x}時の{y}は{z}'

if __name__ == '__main__':
    x = 12
    y = '気温'
    z = 22.4
    print(gen_sentence(x, y, z))