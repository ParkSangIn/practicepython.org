target_age = 100

year_now = input("Enter this year : ")
name = input("Enter your name : ")
age = input("Enter your age : ")

print("{2}, you might be {0} years old at {1} year.".
	format(target_age, target_age - int(age) + int(year_now), name))

input_str = input("Enter a string that you want to print : ")
number_repeat = input("Enter a number of what you want to repeat : ")

print((input_str + '\n') * int(number_repeat))
