num = int(input("Enter a number which you want to figure that is even or odd or multiple of 4 : "))

if (num % 4 == 0):
	print("The number is multiple of 4.")
elif (num % 2 == 0):
	print("The number is even.")
else:
	print("The number is odd.")

dividend = int(input("Enter dividend number : "))
divisor = int(input("Enter divisor number : "))

if (dividend % divisor == 0):
	print("There is no remainder.")
else:
	print("There is remainder {}.".format(dividend % divisor))