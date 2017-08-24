bill = float(raw_input("What was the total bill? "))
service = raw_input("Rate the level of service: good, fair, or bad: ")
if service == "good":
    percentage = 0.20

elif service == "fair":
     percentage = 0.15

elif service == "bad":
     percentage = 0.10

tax = bill * percentage
bill  = bill + tax
print "Your total bill: $ " + str("%.2f" % bill)

split = int(raw_input("How many people in the party"))
perPerson = bill / split
print "Amount per person: " + str("%.2f" % perPerson)
