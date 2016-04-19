for x in range(0,101,1): #a loop from 0 to 100
    if x == 0: #if x is 0
        print(x, ' is null') #print null, if x is null
    elif x % 2 != 0: #if x modulo two is not equal to 0
        print(x, ' is odd') #print odd if x is odd
    else: #if everything else fails, the same as "elif x % 2 == 0:"
        print(x, ' is even') #else print even
