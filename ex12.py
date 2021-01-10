import random

def get_first_last_element(l):
	return [l[0], l[-1]]

a = random.sample(range(10),5)

print(a)
print(get_first_last_element(a))