'''
Reads through files and parses out paragraphs (denoted by newline characters)
'''

f = open('workfile', 'r')

text = []

while(line is not ""):
  text += [f.readLine()]

print(text)
