def fizzbuzz():
    for i in range(101):
        if (i % 3 == 0):
            print("Fizz", end="")
        elif (i % 5 == 0):
            print("Buzz", end="")
        else:
            print(f"{i}", end="")
        print(" ", end="")
