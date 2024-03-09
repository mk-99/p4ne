
while True:
    test_string = input("Введите строку: ")
    match test_string:
        case "one":
            print("Введено one")
        case "two":
            print("Введено two")
        case "three" | "four":
            print("Введено three or four")
        case _:
            print("Введено что-то ещё")
