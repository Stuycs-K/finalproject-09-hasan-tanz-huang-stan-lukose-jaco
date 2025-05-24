def index(char):
    if not isinstance(char, int):
        return (ord(char) - ord('A')) % 26
    else:
        return char
def find_integer(integer, array):
    integer = mod26(integer)
    for index, i in enumerate(array):
        #print(str(i) + " and " + str(chr(ord('A') + integer)))
        if (integer == i):
            return index
    print("you're dumb")
    return(-1)
def mod26(integer):
    if (integer >= 0):
        return integer % 26
    else:
        return integer + 26
def encode(char, plugboard, rotors):
    #setup
    rotors[0] = index(rotors[0])
    rotors[1] = index(rotors[1])
    rotors[2] = index(rotors[2])
    old0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    old1 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    old2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    r0 = []
    r1 = []
    r2 = []
    reflector = []
    for i in range(len(old0)):
        r0.append(index(old0[i]))
        r1.append(index(old1[i]))
        r2.append(index(old2[i]))
        reflector.append(index(reflect[i]))
    #going forward
    char = index(char)
    char = (r2[(char + rotors[2]) % 26] - rotors[2])
    char %= 26
    char = r1[(char + rotors[1]) % 26] - rotors[1]
    char %= 26
    char = r0[(char + rotors[0]) % 26] - rotors[0]
    char %= 26
    #reflect
    char = reflector[char]
    #going backward
    char = mod26(find_integer(char + rotors[0], r0) - rotors[0])
    char = mod26(find_integer(char + rotors[1], r1) - rotors[1])
    #print("char is after r1 " + str(char))
    char = mod26(find_integer(char + rotors[2], r2) - rotors[2])

    print(chr(char + ord('A')))

def update(rotors):
    if (rotors[2] == index('V')):
        rotors[1] = mod26(rotors[1] + 1)
        if (rotors[1] == index('E')):
            rotors[0] = mod26(rotors[0] + 1)
    rotors[2] = mod26(rotors[2] + 1)
def enigma(plugboard, rotors):
    string = input("Input: ")
    rotors[0] = index(rotors[0])
    rotors[1] = index(rotors[1])
    rotors[2] = index(rotors[2])
    for i in range(len(string)):
        update(rotors)
        encode(string[i], [], rotors)
enigma([], ['A', 'A', 'A'])