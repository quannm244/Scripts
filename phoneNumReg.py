import re

phoneNumReg = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumReg.search("Here is my phone no (736)-331-3283")
print("Phone number found: "+ mo.group())
print(mo.group(1))
print(mo.group(2))