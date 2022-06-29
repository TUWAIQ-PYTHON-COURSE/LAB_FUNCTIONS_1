def f1(n):
    ''' a function that takes 1 parameter of type int , then it prints out the result formatted '''
    for h in range(n):
        for i in range(n,0, -1):
            print(i , end=' ')
        n -=1
        print("")    
f1(5)
    

