(n, k) = map(int, input().split(' ')) #two input values in the same line

ans = 0

for i in range(n):        
	x = int(input())
	if x % k == 0:     #if remiander == 0
		ans += 1       #incrementing the ans by 1

print(ans)	