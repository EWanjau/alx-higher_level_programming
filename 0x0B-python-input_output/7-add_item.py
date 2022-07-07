#!/usr/bin/python3
"""Module 7-add_item
adds arguments to a python list and save them to a file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
my_file = 'add_item.json'

my_list = load_from_json_file(my_file)

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        my_list.append(i)
save_to_json_file(my_list, my_file)
