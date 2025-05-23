# Rotate letter by a certain caesar shift for a given rotor, then move to the next rotor and cycle through
def rotorShift(str, charRotors):
    shifted = ""
    for i in range(len(str)):
        shifted += char(ord(str[i]) + ord(charRotate[i%3]))
    return shifted

# Swap letters
def plugboard(str, swapSettings):
    # Get letters to swap with each other from the user
