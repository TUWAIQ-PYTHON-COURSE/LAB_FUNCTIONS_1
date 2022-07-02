## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if 
#we give it 5 for example):

#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

### Document the newly created function. describe what it does, then print the documentation.

def half_pyramid(num : int):
    '''half pyramid function start from number 5 to 0'''
    for x in range(num,0,-1):
        for y in range(x,0,-1):
            print(y,end = " ")
        print()
half_pyramid(5)
print(half_pyramid.__doc__)
