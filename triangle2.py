# height = int(raw_input("Enter the number of rows(height) for the triangle? "))
#
# for i in range(height):
#         print ' '*(height-i-1) + '*'*(2*i+1)

def printTriangle(height):
    for i in range(height):
        print ' '*(height-i-1) + '*'*(2*i+1)

printTriangle(10)
