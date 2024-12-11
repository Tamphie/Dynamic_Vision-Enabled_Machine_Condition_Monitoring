import random

secret = random.randint(1,100)
tries = 1
while tries < 6:
    guess = int(input('1-100 ,{:d} input'.format(tries)))
    if guess == secret :
        print("right")
        break
    elif guess > secret :
        print("big")
    else:
        print("small")
    tries += 1
else:
    print("fail")
