import math

def get_integer(help_text="Enter a number : "):
	return int(input(help_text))

num = get_integer()

for i in range(2, int(math.sqrt(num)) + 1):
	if num % i == 0:
		print("There is divisor {}. \n{} is not a prime number.".format(i, num))
		break
else: 
	print("{} is a prime number.".format(num))


