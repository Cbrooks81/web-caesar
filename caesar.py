def alphabet_position(letter):

    alphalower = ('abcdefghijklmnopqrstuvwxyz')
    alphaupper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if letter in alphalower:

        a = alphalower.index(letter)

    elif letter in alphaupper:

        a = alphaupper.index(letter)

    else:

        a = letter

    return a


def rotate_character(char,rot):

    alphalower = ('abcdefghijklmnopqrstuvwxyz')
    alphaupper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if char in alphalower:

        newchar = (alphabet_position(char))
        newchar2 = (newchar + int(rot)) % 26
        newchar3 = alphalower[newchar2]

    elif char in alphaupper:

        newchar = (alphabet_position(char))
        newchar2 = (newchar + int(rot)) % 26
        newchar3 = alphaupper[newchar2]

    else:

        newchar3 = char

    return newchar3

def encrypt(text,rot):


    return ''.join(rotate_character(x,rot) for x in text)
