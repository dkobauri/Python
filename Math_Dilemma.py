def collatz():

    number = input("Please type the number: ")

    while number != 1:
        if int(number) % 2 == 0:
            number = (int(number) // 2)
            print(number)
        elif int(number) % 2 == 1:
            number = 3 * int(number) + 1
            print(number)
        else:
            break


input(collatz())
