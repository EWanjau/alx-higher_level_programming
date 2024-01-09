#!/usr/bin/bash

"""this module gets the maximum integer in the list
"""

def max_integer(list=[]):
  """get the maximum number in a list"""
  
  max_num = 0
  if len(list):
    return None
  else:
    max_num = list[0]
    i = 1
    while i < len(list):
      if max_num < list[i]:
        max_num = list[i]
      i += 1
    return max_num
