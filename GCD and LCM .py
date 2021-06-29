t= int(input())         #enter the number of testcases

# GCD by a recursive function
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)           #inter-changing the a and b values

        #lcm function by using gcd

def lcm(a,b):
	return (a * b )// gcd(a,b)          #lcm = (a*b) // gcd(a,b)

#driver code

for i in range(t):
    c,d=map(int,input().split(' '))            #input two values in the same line
    print(gcd(c,d) , end= " ")              #end parameter outpus the value in the same line
    print(lcm(c,d))