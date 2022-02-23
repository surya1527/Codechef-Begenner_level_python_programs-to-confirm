

n = int(input())
m = int(input())
o = int(input())
sum = n
l = []
for i in range (o):
    l.append(sum)

    sum = n + m
    n = sum
for i in l:
    print(i,end = " ")