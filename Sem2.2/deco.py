print("Start")

def modify_cubic(old_func):
    def new_cubic(arg):
        print("Вычисляем куб от ", arg)
        return old_func(arg)
    return new_cubic

@modify_cubic
def cubic(arg):
   return arg * arg * arg

# cubic = modify_cubic(cubic)

for i in range (0, 10):
    print(cubic(i))
