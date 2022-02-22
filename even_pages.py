# # Python program to print Even Numbers in a List

# # list of numbers
# list1 = [10, 21, 4, 45, 66, 93]

# # iterating each number in list
# for num in list1:

# 	# checking condition
# 	if num % 2 == 0:
# 		print(num, end=" ")




n = 33423968
x = [int(a) for a in str(n)]    #splits the contunuous  numbers into list format

for num in x:
    if num % 2 == 0:
        p = num

        print(p, end="")
