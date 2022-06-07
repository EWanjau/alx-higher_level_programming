#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_out = ()
    if len(sentence) == 0:
        tuple_out = len(sentence), None
        return tuple_out
    else:
        tuple_out = len(sentence), sentence[0]
        return tuple_out
