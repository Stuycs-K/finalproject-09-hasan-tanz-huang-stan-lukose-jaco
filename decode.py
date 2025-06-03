import multiprocessing
import os
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
            if (start - i > 19 or (i < num - 2 and string1[i] in consonants and string1[i + 1] in consonants)):
                continue
            #print("dictionary[\""+ string1[start:i] + "\"] = 1")
            answer = answer + numWords(string1, i) + 1
    return answer

def e(rotors):
    answer = ""
    rotors1 = rotors.copy()
    check = []
    for i in range(len(string)):
        update(rotors)
        answer += encode(string[i], rotors)
    #print(answer)
    return (numWords(answer, 0), answer, rotors1)

glist = [[i, j, k] for i in range(26) for j in range(26) for k in range(26)]
#glist = [[0,0,0]]
def d():
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        contents = pool.map(e, glist)
    return contents

def parseArgs():
    try:
        number = sys.argv[1]
    except IndexError:
        print("Invalid number of arguments")
        return None
    if (len(number) != 3):
        print("Rotor numbers must have length 3")
        return None
    if (not(number.isnumeric())):
        print("Rotor numbers must be numeric")
        return(None)
    if (number[0] == number[1] or number[0] == number[2] or number[1] == number[2]):
        print("Rotor numbers must not repeat")
        return None
    for i in range(len(number)):
        if (int(number[i]) < 1 or int(number[i]) > 5):
            print("Rotor numbers must be greater than 0 and less than 6")
            return None
    number = list(number)
    #print(number)
    return number

arguments = parseArgs()
if (arguments is not None):
    #print(arguments)
    for i in range(len(arguments)):
        r.insert(0, oldr[int(arguments[i]) - 1])
    for i in range(len(r)):
        r[i] = list(r[i])
        for j in range(len(r[i])):
            r[i][j] = index(r[i][j])
            findr[i][r[i][j]] = j
    #print(r)
    contents = d()
    answer = [thing for thing in contents if thing is not None]
    answer = sorted(answer, reverse = True)

    with open("test.txt", "r") as files:
        for i in range(1):
            string = files.readline().strip()
            string = "WXCHWYZBWPGBDEQXOHWFFGVTWBMHOOMJVXXJG"
            contents = d()
            contents = sorted(contents, reverse = True)
            for j in range(3):
                if (len(contents[j][1]) > 30):
                    finalanswer = contents[j][1][:30] + "..."
                else:
                    finalanswer = contents[j][1]
                finalstring = ""
                for m in range(len(contents[j][2])):
                    finalstring += chr(ord('A') + int(contents[j][2][m]))
                print(finalstring + ": " + finalanswer)
