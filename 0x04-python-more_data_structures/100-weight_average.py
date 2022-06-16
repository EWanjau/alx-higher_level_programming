#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight = dict(my_list)
    sum1 = 0
    weight_total = 0
    result = 0
    for k, v in weight.items():
        sum1 += k * v
        weight_total += weight[k]
    result = sum1 / weight_total
    return result
