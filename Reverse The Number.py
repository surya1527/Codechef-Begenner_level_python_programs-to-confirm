t = int(input())        #enter the number of testcases
for i in range (t):

    number = int(input())           #input the nunmber
    rev = 0

    # logic

    while (number>0):
        rev = number %10 + rev * 10     
        number = number // 10
    print(rev)