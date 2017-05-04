def decorator(F):
    def wrapper(arg):
        print("Вычисляем куб от ", arg)
        return F(arg)
    return wrapper

@decorator
def cubic(arg):
   return arg * arg * arg

for i in range (0, 10):
    print(cubic(i))
