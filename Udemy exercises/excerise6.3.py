# Your task is to write a program that:
# (1) opens the essay.txt file in read mode,
# (2) reads its content,
# (3) finds out the number of characters in the content,
# (4) prints out the number of characters.

file = open('essay.txt', 'r')
content = file.read()
num = len(content)
print(num)