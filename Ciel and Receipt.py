t = int(input())   #entre the number of test cases
for i in range (t):

    p = int(input())            #input the number

    l = [2048,1024,512,256,128,64,32,16,8,4,2,1]

    ans= 0

    while(p>0):
        for j in l :
            if (p>=j):
                ans+= p//j
                p%=j
    print(ans)
                