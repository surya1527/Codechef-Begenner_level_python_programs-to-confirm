t=int(input())          #enter the number of testcases
for _ in range(t):
	c=0                     
	s=input()           #string input
	a=s[0:len(s)//2]
	if len(s)%2==0:
		b=s[len(s)//2:]             #stores the 2nd half of the string
	else:
		b=s[(len(s)//2)+1:]         #strores the second half of the satring and ignores the 1st letter
	for i in range(len(a)):
		if a.count(a[i])==b.count(a[i]):
			c+=1
	if len(a)==c:
		print("YES")
	else:
		print("NO")
		