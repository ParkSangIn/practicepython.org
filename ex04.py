#basic
num = int(input("Enter a number : "))

if_exec = False
for i in range(1, num//2 + 1):
	if (num % i == 0):
		print("{} divides evenly into {}".format(i, num))
		if_exec = True

if (not if_exec):
	print("There is no divisor for {}.".format(num))
