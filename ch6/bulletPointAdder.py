#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text in the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')

# Loop through all the indexes in the 'lines' list
for i in range(len(lines)):
    # Add the star to each tring in the 'lines' list
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)