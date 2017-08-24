num = int(raw_input("Enter a number: "))

count = 0
print ("These are the factors for " + str(num))

for x in range(1, num + 1):
    if(num%x == 0):
        print(x)
        count = count + 1

if (count == 0):
    print("The number is prime!")
v
