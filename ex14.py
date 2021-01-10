import random

def remove_duplicates_from_list1(l):
	return list(set(l))

def remove_duplicates_from_list2(l):
	result_l = []
	[result_l.append(i) for i in l if i not in result_l]
	result_l.sort()
	return result_l

#getnerate random list having duplicate elements
list1 = [random.randint(0,5) for i in range(10)]

print("befor removing duplicates : ")
print(list1)
print("after removing duplicates : ")
print(remove_duplicates_from_list1(list1))
print(remove_duplicates_from_list2(list1))


