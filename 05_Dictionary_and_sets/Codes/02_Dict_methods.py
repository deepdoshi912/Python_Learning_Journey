d = {}  #Empty Dicrtionary 

marks = {
    "Deep": 90,
    "Shyam": 80,
    "Rohan": 85,
     0:"deep"         # We can write First int and then string value.
}

print(marks.items()) #It will print items which are keys and values in the form of tuple 

print(marks.keys())  # It will print only key 

print(marks.values()) # It will print only values 

marks.update({"Deep":99})  #Update something into a dictionary 
print(marks)

print(marks.get("Deep"))  #  retuen a value which key we get 

marks.pop("Rohan")
print(marks)
