N = int(input())                        #enter the input
s = map(int, input().split())           #Multiple input values inthe same line

#initilizing the list

a=[]
b=[]

for i in s:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)

if len(a)> len(b):
    print("READY FOR BATTLE")
else:
    print("NOT READY")