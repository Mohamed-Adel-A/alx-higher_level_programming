#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_len = 0

    for i in range(list_lenght)
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wong type")
            result = 0
        finally:
            result_list.append(result)
    return (result_list)
