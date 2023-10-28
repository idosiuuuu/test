bil = int(input('masukkan bilangan :'))

def faktorial(a):
    if a == 1 :
        return(a)
    else:
        return(a*faktorial(a-1))

print('{}! = {}'.format(bil,faktorial(bil)))
print(f'{bil}! = {faktorial(bil)}')