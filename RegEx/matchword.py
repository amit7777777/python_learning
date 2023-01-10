import re

s = 'iprimed: A computer science portal for job seekers'

match = re.search(r'portal', s)

print('Start Index:', match.start())
print('End Index:', match.end())
