def readposint():
    while True:
        try:
            number = input("Enter a positive integer: ")
            if number == "":
                print("No input.")
            else:
                print("Input Accepted.")
            value = int(number)
            if value < 0:
                print("This is not a Positive Integer.")
            else:
                print("This is a Positive Integer.")
                break
        except:
            print("Invalid Input.")

readposint()