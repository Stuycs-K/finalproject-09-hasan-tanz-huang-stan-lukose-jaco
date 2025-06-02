import multiprocessing
import os

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

string = "AMVYBVRDBBWUWIQGDHVKUSYUUQKFVHSXVUH"
consonants = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'M', 'P', 'Q', 'T', 'V', 'X', 'Z']
fconsonants = ['H', 'L', 'N', 'R', 'W', 'Y']

#def illegal():

dictionary = {}
with open ("new.txt", "r") as file:
    for i in range(100000):
        thing = file.readline().strip()
        if (len(thing) != 0):
            dictionary[thing] = 1

def numWords(string1, start):
    answer = 0
    num = len(string1)
    for i in range(start, num):
        text = string1[start:i]
        if (text in dictionary):
            if (i < num - 2 and string1[i] in consonants and string1[i + 1] in consonants or start - i > 19):
                continue
            #print("dictionary[\""+ string1[start:i] + "\"] = 1")
            answer = answer + numWords(string1, i) + 1
    return answer

def e(rotors):
    answer = ""
    check = []
    for i in range(len(string)):
        update(rotors)
        answer += encode(string[i], rotors)
    #print(answer)
    return (numWords(answer, 0), answer)

glist = [[i, j, k] for i in range(26) for j in range(26) for k in range(26)]
#glist = [[15,6,25]]
def d():
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        contents = pool.map(e, glist)
    return contents
contents = d()
answer = [thing for thing in contents if thing is not None]
answer = sorted(answer, reverse = True)

for k in range(1):
    with open("john.txt", "r") as files:
        for i in range(1):
            string = files.readline().strip()
            contents = d()
            contents = sorted(contents, reverse = True)
            print(contents[0])
            print(contents[1])
