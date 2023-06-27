#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers_printed = 0
    for i in range(x):
        try:
            print("{:d}".fromat(mylist[i]), end="")
            numbers_printed += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (numbers_printed)
      
