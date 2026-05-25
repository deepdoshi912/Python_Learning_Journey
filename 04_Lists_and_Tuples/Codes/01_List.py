#In Python, a List is a container that holds an ordered collection of items.
#  It is one of the most commonly used data structures in Python. Lists are mutable, which means you can change their content without changing their identity.

list = ["Apple", "Banana",735, 3.14, True]

print(list) 

print(list[0])
list[0] = "Orange" #Unlike strings, lists are mutable, which means you can change their content without changing their identity.

print(list[0])

# Slicing a list
print(list[1:4]) #This will print the elements from index 1 to index 3 (index 4 is not included).
