#Langrange interpolation formula

n = int(input("Enter the number of data in dataset : "))


li = [[0 for i in range(n)]for i in range(2)]

for i in range(n):
    li[0][i] = int(input("enter the value of x{}  : ".format(i)))
    li[1][i] = int(input("enter the value of y{}  : ".format(i)))

x = int(input("enter the unknown value of x : "))

y = 0

for i in range(n):
    numerator = 1
    denominator = 1
    
    for j in range(n-1):
        if i!=j:
            numerator = numerator * ( x - li[0][j] )
            denominator = denominator * (li[0][i] - li[0][j])
    
    y = y + (numerator/denominator)*li[1][i]

print(y)