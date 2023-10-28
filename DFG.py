def hanoi (n, tiang_awal, tiang_target, tiang__bantu):
    if n == 1:
        print(f'memindahkan cakram 1 dari{tiang_awal} ke {tiang_target}')
    return

    hanoi(n-1, tiang_awal, tiang__bantu, tiang_target)
    print(f'memindahkan cakram {n} dari {tiang_awal} ke {tiang_target}')
    hanoi(n-1, tiang__bantu, tiang_target, tiang_awal)

n = 4
hanoi(n, 'A', 'C', 'B')

