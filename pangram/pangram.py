import string 

def pangram(sentence=None):
    return is_pangram(sentence)

def is_pangram(sentence):
    
    pangramFlag = True

    aleph = list(string.ascii_lowercase)
    for letter in aleph:
        if letter not in sentence.lower():
            pangramFlag = False
            break  

    return pangramFlag
