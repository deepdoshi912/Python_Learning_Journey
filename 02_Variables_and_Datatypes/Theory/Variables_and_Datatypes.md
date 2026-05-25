# Python Variables and Data Types

Variables are used to store data in Python.

## Creating Variables

```python
name = "Deep"
age = 20
```

Here:
- `name` stores string value
- `age` stores integer value

---

# Rules for Variable Names

- Variable name cannot start with number
- Spaces are not allowed
- Use meaningful names
- Underscore `_` can be used

## Correct Examples

```python
user_name = "Deep"
student_age = 20
```

## Wrong Examples

```python
1name = "Deep"
student age = 20
```

---

# Data Types in Python

Python has different data types.

| Data Type | Example |
|---|---|
| Integer (`int`) | `10` |
| Float (`float`) | `5.8` |
| String (`str`) | `"Hello"` |
| Boolean (`bool`) | `True` |

---

# Integer Example

```python
age = 20
print(age)
```

---

# Float Example

```python
height = 5.8
print(height)
```

---

# String Example

```python
name = "Deep"
print(name)
```

---

# Boolean Example

```python
is_student = True
print(is_student)
```

---

# Checking Data Type

Use `type()` function.

```python
age = 20

print(type(age))
```

Output:

```python
<class 'int'>
```

---

# Multiple Variables

```python
x = 10
y = 20
z = 30

print(x, y, z)
```

---

# Taking User Input

```python
name = input("Enter your name: ")

print(name)
```

---

# Type Conversion

Convert one data type into another.

## Integer to String

```python
age = 20

print(str(age))
```

## String to Integer

```python
num = "10"

print(int(num))
```

---

# Important Points

- Variables store values
- Python automatically detects data type
- `type()` checks data type
- `input()` takes user input
- Type conversion changes data type

# Operators, Typecasting and Input Function

# Operators in Python

Operators are used to perform operations on variables and values.

---

# Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 2` |
| `-` | Subtraction | `5 - 2` |
| `*` | Multiplication | `5 * 2` |
| `/` | Division | `5 / 2` |
| `%` | Modulus | `5 % 2` |
| `**` | Power | `5 ** 2` |
| `//` | Floor Division | `5 // 2` |

## Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
```

---

# Comparison Operators

Used to compare values.

| Operator | Example |
|---|---|
| `==` | `a == b` |
| `!=` | `a != b` |
| `>` | `a > b` |
| `<` | `a < b` |
| `>=` | `a >= b` |
| `<=` | `a <= b` |

## Example

```python
a = 10
b = 5

print(a > b)
print(a == b)
```

---

# Logical Operators

| Operator | Meaning |
|---|---|
| `and` | True if both conditions are true |
| `or` | True if one condition is true |
| `not` | Reverses condition |

## Example

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

---

# Assignment Operators

```python
x = 10

x += 5
print(x)

x -= 2
print(x)
```

---

# Typecasting

Typecasting means converting one data type into another.

---

# Integer to Float

```python
a = 10

print(float(a))
```

---

# Float to Integer

```python
b = 5.8

print(int(b))
```

---

# Integer to String

```python
age = 20

print(str(age))
```

---

# String to Integer

```python
num = "50"

print(int(num))
```

---

# Input Function

`input()` function is used to take input from user.

## Example

```python
name = input("Enter your name: ")

print(name)
```

---

# Important Point

`input()` always returns data in string format.

## Example

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```python
<class 'str'>
```

---

# Taking Integer Input

```python
age = int(input("Enter your age: "))

print(age)
```

---

# Taking Float Input

```python
height = float(input("Enter height: "))

print(height)
```

---

# Practice Example

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

---

# Important Points

- Operators perform operations
- Typecasting changes data type
- `input()` takes user input
- `input()` returns string by default
- Use `int()` or `float()` for number input