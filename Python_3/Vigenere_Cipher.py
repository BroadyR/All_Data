###this is a viginere cypher

#range of chr is 0-1114111
#To get the ASCII code of a character, use the ord() function.
#To get the character encoded by an ASCII code number, use the chr() function.



while(True):
    # define/reset some variables

    usr = ""
    key = ""
    plaintext = ""
    cyphertext = ""
    temp = ""

    print("Please type E for encryption, or D for decryption")
    print("Alternatively, type Q to quit")

    usr = input()

    if(usr == "E" or usr == "e"):
        print("You have chosen encryption")

        print("Please enter a plaintext")
        plaintext = input()

        #print("The length of plaintext is ", str(len(plaintext)))

        print("Now, type in a key")
        key = input()

        #ensure that the key is long enough
        key = key * len(plaintext)

        for i in range(len(plaintext)):
            temp = (ord(plaintext[i]) + ord(key[i]))%1114111
            cyphertext += chr(temp)

        print("Your cyphertext is '{}'".format(cyphertext))

    elif(usr == "D" or usr == "d"):
        print("You have chosen decryption")

        print("Please enter a cyphertext")
        cyphertext = input()
        print("Now, type in the key")
        key = input()

        #ensure the key is long enough
        key = key * len(cyphertext)

        for i in range(len(cyphertext)):
            temp = (1114111 + ord(cyphertext[i]) - ord(key[i]))%1114111
            plaintext += chr(temp)

        print(("Your plaintext is '{}'").format(plaintext))


    elif(usr == "Q" or usr == "q"):
        print("Goodbye")
        exit(0)

    else:
        print("invalid response")