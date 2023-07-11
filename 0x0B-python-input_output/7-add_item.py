#!/usr/bin/python3
""" This script adds all arguments to a Python list, and then
save them to a file """
import sys
save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

# Deserializing JSON data from the file and save it in a Python list
try:
    py_list = load_file(filename)
except Exception:
    py_list = []

# Appending the program arguments to the list
py_list.extend(sys.argv[1:])

# Serializing Python list to JSON file
save_file(py_list, filename)
