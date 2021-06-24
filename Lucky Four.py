t= int(input())         # enter the number of testcases
c=[]                #initialize the list
for i in range(t):
    a = input()             #enter the input
    b=a.count("4")
    c.append(b)
for i in c:
    print (i)