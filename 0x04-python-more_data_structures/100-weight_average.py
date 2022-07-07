#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    avrg = 0
    div = 0
    for i in my_list:
        avrg += i[0] * i[1]
        div += i[1]
    return avrg / div
