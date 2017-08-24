import random

print "I am thinking of a number between 1 and 10."
num = int(raw_input("What's the number? "))
myNum = random.randint(1, 10)
tries = 1
while num != myNum:
    if num > myNum:
        print str(num) + " is too high."
    else:
        print str(num) + " is too low."

    num = int(raw_input("What's the number? "))
    tries += 1
    if tries == 5:
        print "You failed to guess in time!"
        break
    if num == myNum:
        print "You guessed my number! It was", myNum
        print "It took", tries, "tries!\n"


    # else:
    #     print "Yes, You win!"


  # if num == myNum:
  #   print "Yes! You win!"
  #   break
  # if num > myNum:
  #   print str(num) + " is too high."
  #   break
  # else:
  #   print str(num) + " is too low."
  #   break
