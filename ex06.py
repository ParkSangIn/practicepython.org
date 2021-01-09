str = input("Enter a string for testing palindrome : ")

for c in range(len(str)//2):
	if str[c] != str[len(str)-c-1]:
		print("This is not a palindrome!")
		break
else: 
	print("This is a palindrome!")

