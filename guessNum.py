print "I am thinking of a number between 1 and 10."
num = int(raw_input("What's the number? "))
myNum = 5
while True:
  if num == myNum:
    print "Yes! You win!"
    break

  else:
    print "Nope, try again."
    num = int(raw_input("What's the number? "))
    

