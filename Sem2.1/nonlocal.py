def f():
    x = 42

    def g():
        nonlocal x
        x = 43

    print("Перед вызовом g: %d" % x)
    print("Вызываем g")
    g()
    print("После вызова g: %d" % x)

x = 3
f()
print("x в основном модуле: %d" % x)
