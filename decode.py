import multiprocessing
import os
import enchant
def index(char):
    return (ord(char) - ord('A')) % 26
#setup
r = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"]
findr = [[0] * 26, [0] * 26, [0] * 26]
reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector = []
for i in range(len(r)):
    r[i] = list(r[i])
    for j in range(len(r[i])):
        r[i][j] = index(r[i][j])
        findr[i][r[i][j]] = j
for i in range(len(reflect)):
    reflector.append(index(reflect[i]))

def mod26(integer):
    return (integer + 26) % 26

def encode(char, rotors):
    #print(rotors)
    #print(char + "  ", end="")
    char = index(char)
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

    return chr(char + ord('A'))

def update(rotors):
    if (rotors[2] == 21):
        rotors[1] = mod26(rotors[1] + 1)
        if (rotors[1] == 4):
            rotors[0] = mod26(rotors[0] + 1)
    rotors[2] = mod26(rotors[2] + 1)

string = "OPCNVBPFFPGTBSPWWZTVMILUNNSKXYVTBUUQSJNLUUYMCHOBZEW"

dictionary = {}
with open ("words.txt", "r") as file:
    for i in range(3000):
        thing = file.readline().strip().upper()
        dictionary[thing] = 1

def enigma(rotors):
    rotors = [rotors // 26 // 26, (rotors // 26) % 26, rotors % 26]
    answer = ""
    thing = False
    for i in range(len(string)):
        update(rotors)
        answer += encode(string[i], rotors)
        #print(answer)
        if (i < 4 and thing == False and i > 1):
            thing = answer in dictionary
        if (i == 5 and thing == False):
            return None
    #print(thing)
    return answer

def decode(string):
    for i in range(26 * 26 * 26):
        enigma(string, [i // 26 // 26, (i // 26) % 26, i % 26])


def d():
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        contents = pool.map(enigma, range(26 * 26 * 26))   
    return contents
contents = d()
answer = [thing for thing in contents if thing is not None]
print(len(answer))
print(answer)