# Rotate letter by a certain caesar shift per rotor
def rotorShift(str, charRotate):
    shifted = ""
    for i in range(len(str)):
        shifted += char(ord(str[i]) + ord(charRotate))
    return shifted
def plugboard(str):
