def index(char):
    return (ord(char) - ord('A')) % 26
#setup
r = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
findr = [[0] * 26] * 3
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector = []
for i in range(len(r)):
    r[i] = list(r[i])
    for j in range(len(r[i])):
        r[i][j] = index(r[i][j])
        findr[i][r[i][j]] = j
for i in range(len(reflect)):
    reflector.append(index(reflect[i]))

print(r[2])
print(findr[2])

def mod26(integer):
    return (integer + 26) % 26
def encode(char, plugboard, rotors):
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
    #going backward
    for i in range(len(r)):
        char = mod26(r[i][findr[i][mod26(char + rotors[i])]] - rotors[i])
    #plugboard again
    char = pb(char, plugboard)
    #print(chr(char + ord('A')), end = "")

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

def enigma(plugboard, rotors):
    string = "the sky is blue and the grass is green. jokic deserves to win mvp"
    for i in range(len(plugboard)):
        for j in range(len(plugboard[i])):
            plugboard[i][j] = index(plugboard[i][j])
    for i in range(len(rotors)):
        rotors[i] = index(rotors[i])
    for i in range(len(string)):
        if ((ord(string[i]) >= ord('A') and ord(string[i]) <= ord('Z')) or (ord(string[i]) >= ord('a') and ord(string[i]) <= ord('z'))):
            update(rotors)
            encode(string[i].upper(), plugboard, rotors)
    #print("")

enigma([['A', 'Z'], ['B', 'Y'], ['C', 'X'], ['D', 'W'], ['E', 'V'], ['F', 'U'], ['G', 'T'], ['H', 'S'], ['I', 'R'], ['J', 'Q']], ['A', 'A', 'A'])