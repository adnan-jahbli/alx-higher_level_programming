#!/usr/bin/python3
"""Module for appending a line in a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function appends a new line after a target string is found.

    Args:
        filename: Name of the file
        search_string: String to search for
        new_string: Line to append
    """

    result_lines = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            result_lines.append(line)
            if line.find(search_string) != -1:
                result_lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(result_lines))
