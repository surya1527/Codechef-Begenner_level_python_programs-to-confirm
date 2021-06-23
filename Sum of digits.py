
t= int (input())      #reads the number of testcases
for i in range(t):
    a=int(input())  #read the input of the user
    sum = 0         #initializing the variable sum
    #logic
    for i in str(a) :         
        sum = sum + int(i)      
    print(sum)