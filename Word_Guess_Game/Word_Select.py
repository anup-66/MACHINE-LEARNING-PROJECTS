
import random
def WordSelect(fname):
    crntword = ''
    while True:
        lines = open('Name.txt').read().splitlines()
        # print(lines)

        word = random.choice(lines).lower()
        if len(word)==fname:
            crntword=word
            break
    return crntword
