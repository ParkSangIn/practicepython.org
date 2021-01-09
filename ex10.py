print("basic:", '-'*20)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

interchage_list = []
[interchage_list.append(c) for c in a if c in b and c not in interchage_list]
print(interchage_list)


print("extra:", '-'*20)
import random

a = random.sample(range(11),5)
b = random.sample(range(11),7)

a.sort()
b.sort()

print(a, b, sep='\n')
print(list(set([c for c in a if c in b])))

