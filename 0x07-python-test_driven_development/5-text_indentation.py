#!/usr/bin/python3
"""
This is the "text indentation" module.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text(str): the text
        Return: TypeError in case the text isn't str type
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
