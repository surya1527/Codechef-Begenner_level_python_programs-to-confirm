t= int(input())                 #enter the number of testcases
for i in range(t):
    num = input()
    if num == num[::-1]:        #reverses the string
        print("wins")
    else:
        print("loses")
