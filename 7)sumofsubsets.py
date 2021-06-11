def sum_of_subset(lst, x, s):
	if (s == 0):
		return True
	if (x == 0):
		return False
	if (lst[x - 1] > s):
		return sum_of_subset(lst, x - 1, s)
	return sum_of_subset(lst, x-1, s) or sum_of_subset(lst, x-1, s-lst[x-1])
lst = [1,2,5,6,8]
s = 8
x = len(lst)
if (sum_of_subset(lst, x, s) == True):
	print("Subset found")
else:
	print("Subset not found")