#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup_3 = ()
    tup_1 = tuple_a + (0, 0)
    tup_2 = tuple_b + (0, 0)
    tup_3 = tup_1[0] + tup_2[0], tup_1[1] + tup_2[1]
    return tup_3
