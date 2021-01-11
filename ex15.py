input_string = input("Enter a string : ")

def reversing_string(s):
	return ' '.join(s.split()[::-1])

print(reversing_string(input_string))

