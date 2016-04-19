c = 1 #a has the value of one
s = 0 #s has the value of zero
print('Enter Numbers to add to the sum.') #prints the instruction to standard output
print('Enter 0 to quit.')
while c != 0: #while the input is not zero
    print('Current Sum:', s) #prints out the current sum
    c = float(raw_input('Number? ')) #asks for a new number to add to s
    s =+ c #adds c to our total sum
print('Total Sum =', s) #prints out our total sum if we quit by typing 0
