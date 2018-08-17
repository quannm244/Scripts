def collatz(number):
	if number % 2 == 0:
		a = number // 2
		print(a)
		return a
	else:
		b = 3 * number + 1
		print(b)
		return b
		
try:
	result = int(input("Please enter the number: "))
except NameError:
	print("Invalid input")
except ValueError:
	print("Invalid input")
else:
	while True:
		result = collatz(result)
		if result == 1:
			break
