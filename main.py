# Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1   
# 1

# ### Document the newly created function. describe what it does, then print the documentation.


# Advanced function
# def num_pattern(num:int):
#     # document the function

#     # make a list of a the numbers
#     listed_usr_input = []
#     for i in range(num):
#         listed_usr_input += [num-i]
    
#     # print the list till empty and decreament the list by 1
#     for i in range(num):
#         # print(listed_usr_input)
#         print(listed_usr_input)
#         listed_usr_input.remove(num-i)
        
#         i+=1
           
# num_pattern(5)



def numPattern(num:int) -> int:
    '''
    [*] Purpose: given a number, the function will print the numbers in a right triangle pattern, in a reverse order.
    [*] Usage: numPattern(num)
    '''
    for i in range(num):
        for j in range(num - i, 0, -1):
            print(j, end=' ')
        print("\r")
    
numPattern(5)
