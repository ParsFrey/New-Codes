import re

x = input('Enter your Thing:')
c = len(re.findall("\w",x))
z = len(re.findall('\S ',x))+1
y = 1
for i in x:
    if i=='\n':
        y = len(i)

print('The Thing has',y,'lines. and',z,'words. and',c,'characters')
