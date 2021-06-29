try:                                    #try block lets you test a block of code for errors
    n=int(input())                  #enter the number of testcases
    for i in range(n):              
        a=input()           #input string

        #conditions

        if a=='B' or a=='b':
            print("BattleShip")
        elif a=='C' or a=='c':
            print("Cruiser")
        elif a=='D' or a=='d':
            print("Destroyer")
        elif a=='F' or a=='f':
            print("Frigate")
except:                                 #The except block lets you handle the error
    pass
