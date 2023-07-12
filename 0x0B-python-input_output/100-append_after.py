#!/usr/bin/python3
""" 13. Search and update """


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """
    file_text = ""
    with open(filename) as f:
        for line in f:
            file_text += line
            if search_string in line:
                file_text += new_string
    with open(filename, "w") as fw:
        fw.write(file_text)
