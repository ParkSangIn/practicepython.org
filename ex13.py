def get_fibonnaci(n):
	if n == 1:
		return [1]
	elif n == 2:
		return [1,1]
	else:
		l_fibonnaci = [1, 1]
		[l_fibonnaci.append(l_fibonnaci[-1] + l_fibonnaci[-2]) for i in range(n - 2)]
		return l_fibonnaci

n = int(input("Enter a number : "))

print(get_fibonnaci(n))