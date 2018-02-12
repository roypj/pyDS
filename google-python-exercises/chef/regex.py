import re as re
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[a-zA-Z-_]+@\w+\.com', str)
if match:
    print (match.group())  
