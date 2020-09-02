import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

#find me an @ sign followed by some numbers of nonblank characters
# and i dont want the @ sign, i want after the @ sign and up to the
# rest of the nonblank characters
#[^ ] means first character is not space
y=re.findall('@([^ ]*)', lin)

#y=re.findall('^From .*@([^ ]*)', lin)
print(y)
