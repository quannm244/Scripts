inventory = {'rope':2,'torch':6,'gold coin':44,'dagger':30,'arrow':14}

def showInventory(inventory):
	print("Inventory: ")
	total = 0
	for k,v in inventory.items():
		print(str(v)+ ' '+ k)
		total = total + v
	print("Total items: "+str(total))

def addToInventory(inventory, addedItems):
	for k in inventory.keys():
		for i in addedItems:
			if i == k:
				inventory[k] += 1
	return inventory
	
showInventory(inventory)
addedItems=['gold coin','rope','dagger']
addToInventory(inventory,addedItems)
showInventory(inventory)
