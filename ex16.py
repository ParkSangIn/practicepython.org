import random
import string

def pw_generator(size = 12, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join([random.choice(chars) for _ in range(size)])

print(pw_generator(int(input("Enter a number for the digits of your password : "))))