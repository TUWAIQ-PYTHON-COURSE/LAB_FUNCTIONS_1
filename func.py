

def halftri(num : int) -> None:
    '''This function print the entered input as a half tringle'''
    for col in range(num, 0, -1):
        for row in range(col,0,-1):
            print(row, end=" ")
        print()

halftri(5)
print(halftri.__doc__)