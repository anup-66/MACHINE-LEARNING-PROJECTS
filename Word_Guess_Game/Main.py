from Word_Select import WordSelect
def CharCheck(Char, Word):
    if (Char in Word):
        print("Yes this is in the word Go on.")
        return True
    else:
        print("No this letter is not in the word")
        return False

def DisplayWord(char,woord,length,str):
    Sstr = str
    ccount=0
    for chaar in woord:

        if char==chaar:
            # Sstr.replace(Sstr[ccount],char)
            if not (str[ccount]==char):
                Sstr= Sstr[:ccount]+ char+Sstr[ccount+1:]
                break
        ccount += 1
    return Sstr


print("--------------------------------Lets Start the Game fellas----------------------------")
Name = input("Enter Your Name: ")
print("welcome {0} ".format(Name))
while(True):
    try:
        WordLength = int(input("Enter the length of Word btw[4,16]: "))
        MinAttempts = int(input("Enter the min attempts btw[1,25]: "))
        if(WordLength>=4 and MinAttempts<=25 and MinAttempts>=1 and WordLength<=16):
            break
        else:
            print("pls Enter Numbers Within th prameters")
    except:
        print("Enter Valid no")
str = '*'*WordLength
print("This is your Selected Word length : ",str)
print("Now Start Guessing the letters to fill the word")
count=0
Word = WordSelect(WordLength)

while MinAttempts!=0:
    try:
        Char = input("Enter your letter: ")

        Cond =CharCheck(Char,Word)
        if Cond:
            # Correct = DisplayWord(Char,Word,WordLength)
            str=DisplayWord(Char,Word,WordLength,str)
            print("This is How Your Word Looks Like: ", str)
            count+=1
        else:
            MinAttempts-=1
            print("You have ", MinAttempts, " Attempts left to guess")
        if MinAttempts==0:
            print("This was the word " ,Word)
            print("Better lick next time")
            break
        elif (count==WordLength):
            print("You won !")
            print("---------------Game Over----------------------")
            break

    except:
        print("Enter Valid letters")








