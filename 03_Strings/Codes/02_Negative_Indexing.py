name = "Deep"

# This will print "Dee" because it starts from the 4th last character and goes up to the 1st last character (not including it)
print(name[-4:-1]) 

# This will print "eep" because it starts from the 1st character and goes up to the 4th character (not including it)
print(name[1:4]) 

# It starts from zero and goes up to the 4th character (not including it), so it will print "Deep"
print(name[:4])

# It starts from 1 and return the result until the end of the string.
print(name[1:])


str= 'abcdefghijklmnopqrstuvwxyz'
print(str[1:7:4]) # This will print "13" because it starts from the 1st character and goes up to the 5th character (not including it) with a step of 2.
