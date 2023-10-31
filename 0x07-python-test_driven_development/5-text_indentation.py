#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimeter = ".:?"""
    new_text = ""
    add_newline = False

    for char in text:
        if char in delimeter:
            new_text += char + "\n\n"
            add_newline = True
        elif char == " " and add_newline:
            continue
        else:
            new_text += char
            add_newline = False

    print(new_text, end="")
