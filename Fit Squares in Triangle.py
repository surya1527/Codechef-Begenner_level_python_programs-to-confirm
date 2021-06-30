t= int(input())         #enter the number of testcses
for i in range(t):
    b = int(input())        #enter the base input
    b = b-2                 #substracting the extra base from the base of triangle
    t= b//2
    ans= t*(t+1)//2         #sum of n numbers
    print(ans)