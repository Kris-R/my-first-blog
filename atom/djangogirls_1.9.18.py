# DjangoGirls code for 1.9.18 (dates are formatted in US standard)


import random
import string

Name = ""

for i in range(3): # range() is non-inclusive in the upper end.
    Name += random.choice(string.ascii_lowercase)

print(Name)
