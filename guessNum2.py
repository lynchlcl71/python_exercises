pprint "I am thinking of a number between 1 and 10."
num = int(raw_input("What's the number? "))
myNum = 5
while True:
  if num == myNum:
    print "Yes! You win!"
    break
  if num > myNum:
    print str(num) + " is too high."
    break
  else:
    print str(num) + " is too low."
    break
