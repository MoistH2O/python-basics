#This calculator uses most of the common coding syntax with the exception of "for"
print('This is a custom calculator')
anumcorrect = 0
while anumcorrect == 0:
    anum = int(input('Enter a number: '))
    sanum = str(anum)
    print('The number you entered is: [' + sanum +']')
    aiscorrect = input("Is this correct?: ")
    if aiscorrect.upper() == 'YES' or aiscorrect.upper() == 'Y' or aiscorrect.upper() == 'TRUE':
        anumcorrect += 1
    else:
        print('Type it in again then')
optcorrect = 0
while optcorrect == 0:
    operator = input('What would you like to do with this number?: ')
    if operator.upper() == "ADD" or operator.upper() == "PLUS" or operator == "+":
        print("You've decided to [add]")
        operation = 'add'
        optcorrect += 1
    elif operator.upper() == "SUBTRACT" or operator.upper() == "MINUS" or operator == "-":
        print("You've decided to [subtract]")
        operation = 'subtract'
        optcorrect += 1
    elif operator.upper() == "MULTIPLY" or operator.upper() == "TIMES" or operator.upper() == "X" or operator == "*":
        print("You've decided to [multiply]")
        operation = 'multiply'
        optcorrect += 1
    elif operator.upper() == "DIVIDE" or operator.upper() == "/":
        print("You've decided to [divide]")
        operation = 'divide'
        optcorrect += 1
    elif operator.upper() == "POWER" or operator.upper() == "^":
        print("You've decided to raise a [power]")
        operation = 'power'
        optcorrect += 1
    elif operator.upper() == "ROOT":
        print("You've decided to [root]")
        operation = 'root'
        optcorrect += 1
    else:
        print("The operator you've entered is not recognized")
        print("Please try to enter your operator again...")
bnumcorrect = 0
while bnumcorrect == 0:
    bnum = int(input('Enter another number: '))
    sbnum = str(bnum)
    print('The number you entered is: [' + sbnum + ']')
    biscorrect = input('Is this correct?: ')
    if biscorrect.upper() == 'YES' or biscorrect.upper() == 'Y' or biscorrect.upper() == 'TRUE':
        bnumcorrect += 1
    else:
        print('Type it in again then')

if operation == 'add':
    ans = anum+bnum
elif operation == 'subtract':
    ans = anum-bnum
elif operation == 'multiply':
    ans = anum*bnum
elif operation == 'divide':
    ans = anum/bnum
elif operation == 'power':
    ans = anum**bnum
elif operation == 'root':
    ans = bnum**(1/anum)
ans = str(ans)
print('Your result is [' + ans + ']')
goagain = input('Would you like to operate on this answer?: ')
if goagain.upper() == 'YES' or goagain.upper() == 'Y':
    runitagain = 0
    while runitagain == 0:
            optcorrect2 = 0
            while optcorrect2 == 0:
                operator2 = input('What would you like to do with this number?: ')
                if operator2.upper() == "ADD" or operator2.upper() == "PLUS" or operator2 == "+":
                    print("You've decided to [add]")
                    operation = 'add'
                    optcorrect2 += 1
                elif operator2.upper() == "SUBTRACT" or operator2.upper() == "MINUS" or operator2 == "-":
                    print("You've decided to [subtract]")
                    operation = 'subtract'
                    optcorrect2 += 1
                elif operator2.upper() == "MULTIPLY" or operator2.upper() == "TIMES" or operator2.upper() == "X" or operator2 == "*":
                    print("You've decided to [multiply]")
                    operation = 'multiply'
                    optcorrect2 += 1
                elif operator2.upper() == "DIVIDE" or operator2.upper() == "/":
                    print("You've decided to [divide]")
                    operation = 'divide'
                    optcorrect2 += 1
                elif operator2.upper() == "POWER" or operator2.upper() == "^":
                    print("You've decided to raise a [power]")
                    operation = 'power'
                    optcorrect2 += 1
                elif operator2.upper() == "ROOT":
                    print("You've decided to [root]")
                    operation = 'root'
                    optcorrect2 += 1
                else:
                    print("The operator you've entered is not recognized")
                    print("Please try to enter your operator again...")
            anothernumcorrect = 0
            while anothernumcorrect == 0:
                anothernum = int(input('Enter another number: '))
                sanothernum = str(anothernum)
                print('The number you entered is: [' + sanothernum + ']')
                anotheriscorrect = input('Is this correct?: ')
                if anotheriscorrect.upper() == 'YES' or anotheriscorrect.upper() == 'Y' or anotheriscorrect.upper() == 'TRUE':
                    anothernumcorrect += 1
                else:
                    print('Type it in again then')
            ans = int(ans)
            if operation == 'add':
                ans2 = ans + anothernum
            elif operation == 'subtract':
                ans2 = ans - anothernum
            elif operation == 'multiply':
                ans2 = ans * anothernum
            elif operation == 'divide':
                ans2 = ans / anothernum
            elif operation == 'power':
                ans2 = ans ** anothernum
            elif operation == 'root':
                ans2 = anothernum ** (1 / ans)
            ans = ans2
            ans = str(ans)
            print('Your result is [' + ans + ']')
            goagain = input('Would you like to operate on this answer?: ')
            if goagain.upper() == 'YES' or goagain.upper() == 'Y':
                runitagain = 0
            else:
                runitagain += 1
print('Thank you for using this calculator')
