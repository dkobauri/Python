command = ""
started = False

while True:
    command = input("> ").lower()  # DRY = Don't Repeat Yourself!
    if command == "start":
        if started:
            print("Car is Already Started!")
        else:
            started = True
            print("Car Engine Is On And We Are Ready To Go!")
    elif command == "stop":
        if not started:
            print("Car is Already Stopped!")
        else:
            started = False
            print("Car Engine Is Off.")
    elif command == "help":
        print("Start - To Start The Car.")
        print("Stop - To Stop The Car.")
        print("Quit - To Quit.")
    elif command == "quit":
        print("You Left The Car.")
        break
    else:
        print("Sorry, I Don't Understand That...")
