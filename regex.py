### regex ####

import re

patterns = ['term','term1']
text = "this is a string with term"

match = re.search('hello','hello world')

print(match.start())
print(match.end())



split_term = '@'

phrase = "My email is rdelroa@gmail.com"

print(re.split(split_term,phrase))