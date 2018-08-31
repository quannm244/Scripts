#! python3
# program to add bullet points to the start of each line

import pyperclip
text = pyperclip.paste()

lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = str(i+1)+'. ' + lines[i]

text = "\n".join(lines)

pyperclip.copy(text)
