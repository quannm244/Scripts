guess = {
		'Quan':{'apple':10,'lemon':4,'banana':3,'pineapple':1,'watermelon':1},
		'Hung':{'pineapple':2,'banana':4,'watermelon':3},
		'Hai':{'watermelon':2,'apple':4,'lemon':3},
		}

def totalBrought(guess,item):
	total = 0
	for k,v in guess.items():
		total = total + v.get(item,0)
	return total

print("Apple: "+ str(totalBrought(guess, 'apple')))
print("Banana: "+ str(totalBrought(guess, 'banana')))
print("Pineapple: "+ str(totalBrought(guess, 'pineapple')))
print("Lemon: "+ str(totalBrought(guess, 'lemon')))
print("Watermelon: "+ str(totalBrought(guess, 'watermelon')))
	
