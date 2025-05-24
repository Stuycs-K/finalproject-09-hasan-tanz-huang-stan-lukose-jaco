def index(char):
    return (ord(char) - ord('A')) % 26

def encode(char, plugboard, rotors):
    old0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    old1 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    old2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    r0 = []
    r1 = []
    r2 = []
    for i in range(len(old0)):
        r0.append(index(old0[i]))
        r1.append(index(old1[i]))
        r2.append(index(old2[i]))
    char = index(char)
    print("char index is " + str(r2[(char + index(rotors[2]))] % 26))
    char += r2[(char + index(rotors[2])) % 26] - index(rotors[2])
    char %= 26
    print("char is" + str(char)) 
    "C"
    print("char index is " + str((r1[char + index(rotors[1])] % 26)))
    "D"
    char = r1[(char + index(rotors[1])) % 26] - index(rotors[1])
    char %= 26
    print("char is1  " + str(char))
    print("char index is " + str(r1[char + index(rotors[1]) % 26]))
    char = r0[(char + index(rotors[0])) % 26] - index(rotors[0])
    char %= 26
    print(chr(char + ord('A')))

encode('A', [], ['A', 'A', 'C'])