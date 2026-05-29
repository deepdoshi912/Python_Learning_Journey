# Python Dictionary and Sets

# Dictionary in Python

A dictionary is used to store data in key-value pairs.

## Creating Dictionary

```python
student = {
    "name": "Deep",
    "age": 21,
    "course": "Python"
}
```

---

# Accessing Dictionary Values

```python
student = {
    "name": "Deep",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output:

```python
Deep
20
```

---

# Adding New Item

```python
student = {
    "name": "Deep"
}

student["city"] = "Surat"

print(student)
```

---

# Updating Value

```python
student = {
    "age": 20
}

student["age"] = 21

print(student)
```

---

# Removing Item

## pop()

```python
student = {
    "name": "Deep",
    "age": 20
}

student.pop("age")

print(student)
```

---

# Dictionary Methods

## keys()

```python
student = {
    "name": "Deep",
    "age": 20
}

print(student.keys())
```

---

## values()

```python
print(student.values())
```

---

## items()

```python
print(student.items())
```

---

## get()

```python
print(student.get("name"))
```

---

# Loop Through Dictionary

```python
student = {
    "name": "Deep",
    "age": 20
}

for key, value in student.items():
    print(key, value)
```

---

# Nested Dictionary

```python
students = {
    "student1": {
        "name": "Deep",
        "age": 20
    }
}

print(students["student1"]["name"])
```

---

# Sets in Python

A set is a collection of unique values.

- No duplicate values allowed
- Unordered collection

---

# Creating Set

```python
numbers = {1, 2, 3, 4}
```

---

# Adding Element

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

---

# Removing Element

```python
numbers.remove(2)

print(numbers)
```

---

# Set Methods

## union()

Combines two sets.

```python
a = {1, 2}
b = {3, 4}

print(a.union(b))
```

---

## intersection()

Returns common elements.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

---

## difference()

Returns different elements.

```python
a = {1, 2, 3}
b = {2, 3}

print(a.difference(b))
```

---

# Empty Set

```python
empty_set = set()
```

---

# Important Difference

| Dictionary | Set |
|---|---|
| Stores key-value pairs | Stores unique values |
| Uses `{key:value}` | Uses `{value}` |

---

# Important Points

- Dictionary stores data in key-value format
- Sets store only unique values
- Dictionaries are mutable
- Sets are unordered
- Duplicate values are not allowed in sets