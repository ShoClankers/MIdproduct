num = int(input("Enter a number: "))
t = num
numLen = 0
while t>0:
    numLen = numLen + 1
    t = (t/10)
if numLen>4: 
    numLen = int(numLen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk<numLen:
            midOne = rem
        elif chk==numLen:
            midTwo = rem
            num = int(num/10)
            chk = chk + 1
            prod = midOne * midTwo
            print("\nProduct of MId Digits (", midOne, ",", midTwo, ") = ", prod)
        else:
                print("\nNumber does not have enough digits to find middle digits.")