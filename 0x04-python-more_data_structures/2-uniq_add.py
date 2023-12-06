#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = list(set(my_list))
    add = 0
    for i in range(len(uniq)):
        add += uniq[i]
    return add
