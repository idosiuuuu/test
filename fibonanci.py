deret1 = 0
deret2 = 1
n = int(input('masukkan batas deret :'))

for i in range(n):
    print(deret1, end=' ')
    fi = deret2 + deret1
    deret1 = deret2
    deret2 = fi