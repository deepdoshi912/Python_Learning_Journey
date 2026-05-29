
# Union method is use to check the same values in two sets and will return the one set which is in assending order.

s = {1,45,6,8}  #1st set
s1 ={3,54,6,8}  #2nd set

print(s.union(s1))  # Use union method
print(s.intersection(s1))  # Use Intersection method

print({54}.issubset(s1))