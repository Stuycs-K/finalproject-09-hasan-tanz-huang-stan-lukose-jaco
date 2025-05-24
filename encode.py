def index(char):
    return (ord(char) - ord('A')) % 26
def find_integer(integer, array):
    for index, i in enumerate(array):
        print(str(i) + " and " + str(chr(ord('A') + integer)))
        if (integer == i):
            return index
    print("you're dumb")
    return(-1)
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
    char += r2[(char + rotors[2]) % 26] - rotors[2]
    char %= 26
    char = r1[(char + rotors[1]) % 26] - rotors[1]
    char %= 26
    char = r0[(char + rotors[0]) % 26] - rotors[0]
    char %= 26
    print(chr(char + ord('A')))
    #reflect
    char = reflector[char]
    print(chr(char + ord('A')))
    #going backward
    char = find_integer(char + rotors[0], r0) - rotors[0]
    char = find_integer(char + rotors[1], r1) - rotors[1]
    print("char is after r1 " + str(char))
    char = find_integer(char + rotors[2], r2) - rotors[2]

    print(chr(char + ord('A')))

encode('A', [], ['B', 'C', 'H'])