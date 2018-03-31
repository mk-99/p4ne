def f():
    x = 42

    def g():
        nonlocal x
        def i():
            nonlocal y
            y = 46
        x = 43
        y = 45
        i()
        print("После вызова i y=%d" % y)


    print("Перед вызовом g: %d" % x)
    print("Вызываем g")
    g()
    print("После вызова g: %d" % x)

x = 3
f()
print("x в основном модуле: %d" % x)
