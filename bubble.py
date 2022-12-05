import random
count = 0


def compare(t1, t2):  # returns true for disorder
	return t1 > t2 


def check(lst: list, plc: int):
	global count
	count += 1
	if compare(lst[plc], lst[plc+1]):
		temp = lst[plc]
		lst[plc] = lst[plc+1]
		lst[plc + 1] = temp
	return lst	


def complete(lst):
	for i in range(len(lst)-1):
		if compare(lst[i], lst[i+1]):
			return False
	return True


def runt(lst: list):
	for i in range(len(lst)-1):
		# print(lst)
		lst = check(lst, i)
	if complete(lst):
		return lst
	else:
		return runt(lst)


def average(a, reps=100000):
	# reps - the amount of runs, for a more accurate average; a - different number of items in list to sort
	global count
	sum1 = 0
	for i in range(reps):
		mylist = []
		for t in range(a):
			mylist.append(random.randint(0, 99))
		runt(mylist)
		mylist.reverse()
		sum1 += count
		count = 0
	avg = sum1/reps
	return avg  # *100
