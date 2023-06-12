#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_len = len(my_list)
    if (idx < 0 or idx >= list_len):
        return (my_list)
    return(my_list[:idx] + my_list[idx+1:])
