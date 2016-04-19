my_list = ['banana', 'strawberry', 'apple', 'watermelon', 'peach'] #a simple list
sorted_list = sorted(my_list) #python includes powerful sorting algorithms
for x in range(1,11,1): #a for loop which counts to ten
    """range takes up to three arguments: the start, which is
inclusive, the end, which is exclusive and the step size"""
    print(x)
print() #prints an empty line
for y in range(10,0,-1): #the step size can also be negative to count backwards
    print(y)
print()
for z in range(len(sorted_list)): #you can also iterate over lists
    print (sorted_list[z])#prints the list
