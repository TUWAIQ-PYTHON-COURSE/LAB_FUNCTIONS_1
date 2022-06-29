#Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):


def num (n):
    ''' This function that takes 1 parameter of type int , then it prints out the result formatted '''
    for j in range(n):
        for i in range(n,0,-1):
            print(i , end = ' ') 
        n-=1
        print("") 



num(5)