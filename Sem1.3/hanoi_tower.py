def move(source, target, transit, n):
    if n != 0:
        move(source, transit, target, n-1)
        print(n, ": ", source, ' -> ', target)
        move(transit, target, source, n-1)

move(1, 3, 2, 5)
