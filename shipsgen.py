import random as rnd


def pprint(a):
    for i in a:
        print(*i)


def ship(n,s):
    a = []
    for i in range(n):
        s = [0] * n
        a.append(s)
    stx, sty = 0, rnd.randint(0, n - 1)
    a[sty][stx] = 1
    if sty != n//2 + 1 or sty != n//2:
        for i in range(0, abs(sty - n//2)):
            a[i][0] = 1

    x, y = stx, sty
    for i in range(s):
        dir = rnd.randint(1, 4)
        if dir == 1 and y - 1 >= 0 and a[y - 1][x] != 1:
            y -= 1
        elif dir == 2 and x + 1 < n:
            x += 1
        elif dir == 3 and y + 1 < n:
            y += 1
        elif dir == 4 and x - 1 >= 0:
            x -= 1
        a[y][x] = 1
    while 1:
        x = rnd.randint(0, n-1)
        y = rnd.randint(0, n-1)
        if a[y][x] == 1:
            a[y][x] = 0
            break
    return a

def check_ship(a):
    s = 0
    while 1:
        pass

def mirror(a):
    b = []
    for i in a:
        b.append(i[::-1] + i)
    return b