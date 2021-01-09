a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#basic
print("basic:")
for i in a:
	if (i < 5):
		print(i)

#extra1
print("extra1:")
b = []
for i in a:
	if (i < 5):
		b.append(i)
print(b)

#extra2
print('extra2:')
print([i for i in a if i < 5])

#extra3
print("extra3:")
num = int(input("Enter a number : "))
print([i for i in a if i < num])
