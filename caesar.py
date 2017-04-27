def alphabet_position(letter):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = 0
    number = 0
    for all in alphabet_upper:
        if letter == alphabet_upper[x]:
            number = x
            return number
        elif letter == alphabet_lower[x]:
            number = x
            return number
        else:

            x = x + 1
            number = x
    return number

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter = char

    if alphabet_position(letter) == 26:
        return char
    elif char == char.upper():
        rotate = alphabet_position(letter) + rot
        if rotate < 26:
            char = alphabet_up[rotate]
            return char
        else:
            char = alphabet_up[rotate %26]
            return char
    elif char == char.lower():
        rotate = alphabet_position(letter) + rot
        if rotate < 26:
            char = alphabet[rotate]
            return char
        else:
            char = alphabet[rotate%26]
            return char

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = rotate_character(char, rot)
            encrypted = encrypted + pos
    return encrypted
