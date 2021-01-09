#basic
print("basic:")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a) & set(b)))

#extra1
print("extra1:")
import random
num = int(input("Enter a maximum number of numbers you want to create in two random lists : "))
coverage = int(input("Enter a maximum limit size of elements : "))

dic1 = random.sample(range(1, coverage + 1), random.randint(1, num))
dic2 = random.sample(range(1, coverage + 1), random.randint(1, num))

dic1.sort()
dic2.sort()

print(dic1, dic2, sep='\n')

print("Intersection of two lists : {}".format(list(set(dic1) & set(dic2))))

#extra2
print("extra2:")
print(list(set([m for m in a if m in b])))
