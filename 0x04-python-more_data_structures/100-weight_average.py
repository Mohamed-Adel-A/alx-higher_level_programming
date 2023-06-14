#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    weight_sum = 0
    score_sum = 0
    for t in my_list:
        weight_sum += t[0] * t[1]
        score_sum += t[0]
    return (weight_sum / score_sum)
