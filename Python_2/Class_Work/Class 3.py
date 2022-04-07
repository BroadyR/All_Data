from random import randint

numbers = []
while (len(numbers) < 20):
    numbers.append(randint(1,99))

print numbers

num = input("What interger would you like to search for? ")

for index in range(len(numbers)):
                if (numbers[index] == num):
                  print "The valuse is {} was found. ".format(num)
                else:
                    print "{} is not found.".format(num)
                    break
