# Python Lists and Tuples

# Lists in Python

A list is used to store multiple values in a single variable.

## Creating List

```python
numbers = [10, 20, 30, 40]
```

---

# Accessing List Elements

```python
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
```

Output:

```python
10
20
```

---

# Negative Indexing

```python
numbers = [10, 20, 30]

print(numbers[-1])
```

Output:

```python
30
```

---

# List Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```python
[20, 30, 40]
```

---

# Changing List Elements

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

Output:

```python
[10, 50, 30]
```

---

# List Methods

## append()

Adds element at end.

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

---

# insert()

Adds element at specific position.

```python
numbers = [10, 20]

numbers.insert(1, 15)

print(numbers)
```

---

# remove()

Removes element.

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

---

# pop()

Removes last element.

```python
numbers = [10, 20, 30]

numbers.pop()

print(numbers)
```

---

# sort()

Sorts list.

```python
numbers = [40, 10, 30]

numbers.sort()

print(numbers)
```

---

# reverse()

Reverses list.

```python
numbers = [10, 20, 30]

numbers.reverse()

print(numbers)
```

---

# Length of List

```python
numbers = [10, 20, 30]

print(len(numbers))
```

---

# Loop Through List

```python
numbers = [10, 20, 30]

for item in numbers:
    print(item)
```

---

# Tuples in Python

A tuple is similar to list but immutable.

Immutable means values cannot be changed.

## Creating Tuple

```python
numbers = (10, 20, 30)
```

---

# Accessing Tuple Elements

```python
numbers = (10, 20, 30)

print(numbers[0])
```

---

# Tuple Methods

## count()

Counts occurrences.

```python
numbers = (10, 20, 10)

print(numbers.count(10))
```

---

# index()

Returns index value.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

---

# Difference Between List and Tuple

| List | Tuple |
|---|---|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can change values | Cannot change values |

---

# Nested List

```python
data = [[1, 2], [3, 4]]

print(data[0])
```

---

# Taking List Input

```python
numbers = input("Enter numbers: ").split()

print(numbers)
```

---

# Important Points

- Lists are mutable
- Tuples are immutable
- Lists use square brackets `[]`
- Tuples use parentheses `()`
- Many built-in methods are available