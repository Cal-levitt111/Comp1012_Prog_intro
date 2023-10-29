# -*- coding: utf-8 -*-

def string_to_morse_code(x):
    """
    Returns the morse code of a string x.
    If x is not a string, returns 'ValueError, string expected!'.
    """

    mcode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
             'K': '-.-', 'L': '.-..', 'M': '--',   'N': '-.', 'O': '---',
             'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
             'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---',
             '3': '...--', '4': '....-',  '5': '.....',  '6': '-....',
             '7': '--...', '8': '---..',  '9': '----.',  '&': '.-...',
             "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
             ':': '---...', ',': '--..--', '=': '-...-',  '!': '-.-.--',
             '.': '.-.-.-', '-': '-....-', '+': '.-.-.',  '"': '.-..-.',
             '?': '..--..', '/': '-..-.'}

    morse_code = ""

    if type(x) is not str:

        return ("ValueError, string expected")

    for character in list(x):

        if character == " ":
            morse_code += " "

        else:
            morse_code += mcode.get(character.upper())

        morse_code += " "

    morse_code = morse_code[:-1]

    return morse_code

print(string_to_morse_code("Hello world!"))