import re

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("I  just watched Batman")
print(mo.group())
mo1 = batRegex.search("I just watched Batwowoman")
print(mo1.group())
