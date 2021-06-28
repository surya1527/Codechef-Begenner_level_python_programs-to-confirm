t=int(input())                      #enter the number of testcases
notes = [100,50 ,10,5,2,1]
while(t!=0):
    result=0
    a=int(input())                  #enter the input
    for i in notes:
        if a>=i:
            result = result + a//i          #adding the value to result
            a=a%i
    print(result)
    t-=1                            #decrementing the testcases

