try:
    import datetime
    now = datetime.datetime.now()

    # print(f"{now.year}.{now.month}.{now.day} - {now.hour}:{now.minute}:{now.second}")
    # 2020.11.10 - 16:40:54

    Birth_year = input("Birth Year: ")
    age = int(now.year) - int(Birth_year)

    print("Your Age is: " + str(age) + ".")
except ValueError:  # can be added several exceptions.
    print("Invalid Value")
