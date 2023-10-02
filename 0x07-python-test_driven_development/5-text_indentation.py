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
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.strip()
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end="")

