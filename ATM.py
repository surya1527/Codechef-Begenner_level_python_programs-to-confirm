x,y=map(float,input().split()) #two input values in the same line
if x%5==0:
    if(y>=(x+0.5)):
        y -= (x+0.5)     # y = y - (x+0.5) 
print("%.2f"%y)