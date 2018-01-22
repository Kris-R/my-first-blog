# dates in filename as US format
# New DjangoGirls code
# Takes a first-name, last-name input and adds to a dict using first-name
# as key, last-name as value.


nameDict = {}

Name = input("What's you're first and last name? ")

split = Name.split(" ")
print(split)
nameDict.update({split[0] : split[1]})
print(nameDict)
