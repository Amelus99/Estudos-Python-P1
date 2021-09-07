a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

maior_ab = (a + b + abs(a - b)) // 2

maior_abc = (maior_ab + c + abs(maior_ab - c)) // 2

print(maior_abc, 'eh o maior')
