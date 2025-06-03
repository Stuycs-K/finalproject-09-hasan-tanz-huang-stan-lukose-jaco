import sys

def index(char):
    return (ord(char) - ord('A')) % 26
#setup
oldr = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "VZBRGITYUPSDNHLXAWMJQOFECK"]
r = []
findr = [[0] * 26, [0] * 26, [0] * 26]
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector = []
for i in range(len(reflect)):
    reflector.append(index(reflect[i]))

def mod26(integer):
    return (integer + 26) % 26

def encode(char, plugboard, rotors):
    #print(rotors)
    #print(char + "  ", end="")
    char = index(char)
    #plugboard
    char = pb(char, plugboard)
    #print("char is now " + str(char))
    #going forward
    for i in range(len(r) - 1, -1, -1):
        char = r[i][(char + rotors[i]) % 26] - rotors[i]
        char %= 26
    #reflect
    char = reflector[char]
    #print("char is " + chr(char + ord('A')))
    #going backward
    for i in range(len(r)):
        #print("the mod is" + str(mod26(char + rotors[i])))
        char = mod26(findr[i][mod26(char + rotors[i])] - rotors[i])
        #print("char is " + chr(char + ord('A')))

    #plugboard again
    char = pb(char, plugboard)
    return chr(char + ord('A'))

def pb(char, plugboard):
    for i in plugboard:
        #print("length is " + str(len(i)))
        for j in range(len(i)):
            #print(str(i[j]) + " and " + str(char))
            if (i[j] == char):
                return i[len(i) - j - 1]
    return char

def update(rotors):
    if (rotors[2] == index('V')):
        rotors[1] = mod26(rotors[1] + 1)
        if (rotors[1] == index('E')):
            rotors[0] = mod26(rotors[0] + 1)
    rotors[2] = mod26(rotors[2] + 1)

def parseArgs():
    values = []
    try:
        plugboard = sys.argv[1]
        number = sys.argv[2]
        rotors = sys.argv[3]
    except IndexError:
        print("Invalid number of arguments")
        return None
    plugboard = plugboard.upper().strip()
    rotors = rotors.upper().strip()
    if (len(plugboard) != 0):
        try:
            plugboard1 = plugboard.split(' ')
        except ValueError:
            print("Plugboard must be pairs of letters that never repeat separated by a single space in between")
            return None
        plugboard2 = list(plugboard)
        for i in range(len(plugboard2)):
            if ((i % 3 == 2 and plugboard2[i] != ' ') or (i % 3 != 2 and (not (ord(plugboard2[i]) >= ord('A') and ord(plugboard2[i]) <= ord('Z')) or plugboard2[i] in plugboard2[:i]))):
                print("Plugboard must be pairs of letters that never repeat separated by a single space in between")
                return None
        plugboard = [list(joe) for joe in plugboard1]
    else:
        plugboard = []
    if (len(number) != 3):
        print("Rotor numbers must have length 3")
        return None
    if (not(number.isnumeric())):
        print("Rotor numbers must be numeric")
        return(None)
    if (number[0] == number[1] or number[0] == number[2] or number[1] == number[2]):
        print("Rotor numbers must not repeat")
        return None
    number = list(number)
    if (len(rotors) != 3):
        print("Rotor settings must have length 3")
        return None
    rotors = list(rotors)
    for i in range(len(rotors)):
        if (not(ord(rotors[i]) >= ord('A') and ord(rotors[i]) <= ord('Z'))):
            print("Rotor settings must be 3 consecutive letters")
            return(None)
    return [plugboard, number, rotors]

def enigma(string):
    answer = ""
    for i in range(len(string)):
        if ((ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z')) or (ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'))):
            update(rotors)
            answer += encode(string[i].upper(), plugboard, rotors)
    return answer

arguments = parseArgs()
if (arguments is not None):
    plugboard = arguments[0]
    rotors = arguments[2]
    print(plugboard)
    print(arguments)
    for i in range(len(arguments)):
        r.insert(0, oldr[int(arguments[1][i]) - 1])
    print(r)
    for i in range(len(r)):
        r[i] = list(r[i])
        for j in range(len(r[i])):
            r[i][j] = index(r[i][j])
            findr[i][r[i][j]] = j
    for i in range(len(plugboard)):
        for j in range(len(plugboard[i])):
            plugboard[i][j] = index(plugboard[i][j])
    for i in range(len(rotors)):
        rotors[i] = index(rotors[i])
    #print(r)
    if (arguments != None and len(arguments) == 3):
        thing = input("Input: ")
        print(enigma(thing))
