t=int(input())                                  #enter the number of testcases
for i in range (t):                             
    A , B = map(int,input().split())            #two input values in same
    if (A < B):
        print ("<")                             
    elif (A > B):
        print(">")
    elif (A == B):
        print("=")
 
