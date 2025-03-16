import random
import string

alphabets_L = string.ascii_lowercase
alphabets_U = string.ascii_lowercase.upper()
digits = string.digits
symbols = string.punctuation

def strtolist(a):
    l = []
    for i in a:
        l.append(i)
    return l;

def listtostr(a):
    s = ''
    for i in a:
        s += i
    return s

# Four levels of password difficulty:

# 1. Easy

# 2. Moderate

# 3. Strong

# 4. Super-Strong

def removeUpperCase(Pass, upper):
    Pass = strtolist(Pass)
    l = []
    for i in range(upper):
        l.append(alphabets_L[random.randint(0,len(alphabets_L)-1)])
    
    count = 0
    for i in range(len(Pass)):
        if Pass[i] in alphabets_U:
            Pass[i] = l[count]
            count += 1
    

    return listtostr(Pass)

def removePunctuation(Pass, punc):
    Pass = strtolist(Pass)
    l = []
    for i in range(punc):
        l.append(alphabets_L[random.randint(0,len(alphabets_L)-1)])
    
    count = 0
    for i in range(len(Pass)):
        if Pass[i] in symbols:
            Pass[i] = l[count]
            count += 1
    return listtostr(Pass)


def removeDigits(Pass, punc):
    Pass = strtolist(Pass)
    l = []
    for i in range(punc):
        l.append(alphabets_L[random.randint(0,len(alphabets_L)-1)])
    
    count = 0
    for i in range(len(Pass)):
        if Pass[i] in digits:
            Pass[i] = l[count]
            count += 1
    return listtostr(Pass)


while True:
    charnum = input("Please enter the number of characters you want in your password: ")
    try:
        charnum = int(charnum)
    except:
        print("Please enter a real integer value.")
        continue
    
    numbers = input("Do you want numbers in your password (y/n): ")

    if numbers == 'y':
        digitsbool = True
    elif numbers == 'n':
        digitsbool = False
    else:
        print("Please enter either 'y' or 'n'")
        continue

    punctuations = input("Do you want symbols in your password (y/n): ")

    if punctuations == 'y':
        puncbool = True
    elif punctuations == 'n':
        puncbool = False
    else:
        print("Please enter either 'y' or 'n'")
        continue
    
    case = input("Do you want mixed cASeS in your password (y/n): ")

    if case == 'y':
        casebool = True
    elif case == 'n':
        casebool = False
    else:
        print("Please enter either 'y' or 'n'")
        continue

    # digitsbool
    # casebool
    # charnum
    # puncbool

    Password = ""

    checks = 0

    if casebool:
        checks +=1
    if puncbool:
        checks += 1
    if digitsbool:
        checks += 1
    nUpperCase = 0
    nPunctuations = 0
    ndigits = 0
    for i in range(charnum):
        choice = random.randint(0,3)
        if choice == 0:
            Password += alphabets_L[random.randint(0,len(alphabets_L)-1)]
        elif choice == 1:
            Password += alphabets_U[random.randint(0,len(alphabets_U)-1)]
            nUpperCase += 1
        elif choice == 2:
            Password += symbols[random.randint(0,len(symbols)-1)]
            nPunctuations += 1
        elif choice == 3:
            Password += digits[random.randint(0,len(digits)-1)]
            ndigits += 1

    
    if not casebool:
        Password = removeUpperCase(Password, nUpperCase)
    if not digitsbool:
        Password = removeDigits(Password, ndigits)
    if not puncbool:
        Password = removePunctuation(Password, nPunctuations)

    print(Password)

    if checks == 0:
        print("Password Difficulty: Easy")
    if checks == 1:
        print("Password Difficulty: Medium")
    if checks == 2:
        print("Password Difficulty: Hard")
    if checks == 3:
        print("Password Difficulty: Super-Hard")

    lastchoice = input("Do you want to use this program again? (y/n): ")
    if lastchoice == 'y':
        continue
    elif lastchoice == 'n':
        break
    else:
        print("Please enter either 'y' or 'n'")
        break
