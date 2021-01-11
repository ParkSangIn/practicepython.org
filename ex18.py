import random
import string

random_number = ''.join([str(random.randint(0,9)) for _ in range(4)])

# print(random_number)

c = 0

while (True):
	cow = 0
	bull = 0
	input_number = str(input("Enter a number : "))
	c += 1

	for i in range(len(input_number)):
		if input_number[i] == random_number[i]:
			cow += 1
		elif input_number[i] in random_number:
			bull += 1

	print("{} cow, {} bull.".format(cow, bull))
	print("You guessed {} times.".format(c))

	if cow == 4:
		print("congratulation! : {}".format(random_number))
		break
	

