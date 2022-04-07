from random import randint, seed

seed(123456)
for i in range(1,101):
    print "{}\t".format(randint(0, 99)),
    if (i % 10 == 0):
        print
print

seed(123456)
for i in range(1, 101):
    print "{}\t".format(randint(0, 99)),
    if (i % 10 == 0):
        print
seed(randint(0, 65535))
