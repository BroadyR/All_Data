LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def import_scrambled_words():
    scrambledWords = []
    try:
        file = open("D:\\School\\CSC 442\\scrambled.txt", "r") #location of your scrambled word file
        fileContents = file.readlines() #read text file and store each new line as a string
    finally:
        file.close()
    for i in range(len(fileContents)):
        scrambledWords.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return scrambledWords

def Decrypt(scrambledWords):   
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in scrambledWords:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
    print('Hacking key #%s: %s' % (key, translated))
Decrypt()