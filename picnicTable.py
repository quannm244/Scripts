def printItems(itemList, leftWidth, rightWidth):
	print('Picnic Items'.center(leftWidth+rightWidth,'-'))
	for k,v in itemList.items():
		print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth,'.'))

itemList = {'Apple':5,'Spoon':6,'Snack':9,'Drink':300}
printItems(itemList, 11, 5)
