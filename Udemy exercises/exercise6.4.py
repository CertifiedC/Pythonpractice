# Your task is to write a program that:
#
# (1) opens the essay.txt file in read mode,
#
# (2) reads its content,
#
# (3) finds out the number of characters in the content,
#
# (4) prints out the message "The file contains x characters." where x should be the number of characters.
#
# Here is the expected output:
#
# The file contains 144 characters.

file = open('essay.txt', 'r')
content = file.read()
num = len(content)
print(f"The file contains {num} characters.")