def transfer(list):
	string = ''
	for i in range(len(list)):
		if i == len(list)-1:
			string += 'and ' + list[i]
			break
		else:
			string += list[i] + ', '
	return string

spam = ['apples','banana','pineapple','lemon','watermelon']
a = transfer(spam)
print(a)

