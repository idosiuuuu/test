def pangkat(x,y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x,y-1)
x = int(input('masukkan nilai x :'))
y = int(input('masukkan nilai y :'))

print(f'{x} dipangkatkan {y} = {pangkat(x,y)}')