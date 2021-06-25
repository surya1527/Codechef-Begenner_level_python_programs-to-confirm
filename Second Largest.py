n=int(input())              #input thw number of testcases
l =[]                   #initializing the list
for i in range(n):
    l=list(map(int,input().split()))        #two inputs in single line
    l.sort()                    #sorts the list
    print(l[-2])            #prints the last second element in thge list
    