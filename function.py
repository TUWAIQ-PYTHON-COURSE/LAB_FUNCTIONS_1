# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

#5 4 3 2 1   
#4 3 2 1   
#3 2 1   
#2 1   
#1   

### Document the newly created function. describe what it does, then print the documentation. 

def number(num : int):
    """ Ceate a function of 1 parameter that will be return from 5 to 1 """
    for i in range(num, 0 ,-1):
        for j in range(i , 0, -1):
            print(j, end=' ')
        print()

number(5)

print(number.__doc__)