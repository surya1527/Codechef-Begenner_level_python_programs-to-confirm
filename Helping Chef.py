try:                                                #try block tests the block of code
    for i in range(int(input())):
        n=int(input())                              #enter the value
        if n>10 or n==10:
            print("-1")
        else:
            print("Thanks for helping Chef!")
except:                                             
    pass