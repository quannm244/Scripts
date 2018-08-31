#! python3
# pw.py - Insecure password locker program

passwords = {'email': 'applelovekem',
			'capu':'Pumitun123a@A',
			'nec':'8fb2e1ec250f'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] copy account password')
	sys.exit()

account = sys.argv[1]

if account in passwords:
	pyperclip.copy(passwords[account])
	print("Password for "+account+ " copied to clipboard.")
else:
	print("There is no account named "+account)
