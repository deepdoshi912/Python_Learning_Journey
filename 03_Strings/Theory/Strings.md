# Python Strings

A string is a sequence of characters enclosed in quotes.

## Examples

```python
name = "Deep"
city = 'Surat'
```

---

# Creating Strings

```python
str1 = "Hello"
str2 = 'Python'
```

---

# Printing String

```python
name = "Deep"

print(name)
```

---

# String Indexing

Each character has an index number.

```python
word = "Python"

print(word[0])
print(word[1])
```

Output:

```python
P
y
```

---

# Negative Indexing

```python
word = "Python"

print(word[-1])
```

Output:

```python
n
```

---

# String Slicing

Used to get part of string.

## Syntax

```python
string[start:end]
```

## Example

```python
name = "Python"

print(name[0:3])
```

Output:

```python
Pyt
```

---

# String Functions

## Length Function

```python
name = "Python"

print(len(name))
```

---

# Uppercase

```python
text = "hello"

print(text.upper())
```

---

# Lowercase

```python
text = "HELLO"

print(text.lower())
```

---

# Capitalize

```python
text = "python"

print(text.capitalize())
```

---

# Replace Function

```python
text = "Hello"

print(text.replace("Hello", "Hi"))
```

---

# Find Function

```python
text = "Python"

print(text.find("t"))
```

---

# Count Function

```python
text = "apple"

print(text.count("p"))
```

---

# String Concatenation

Joining strings using `+`.

```python
first = "Deep"
last = "Doshi"

print(first + " " + last)
```

---

# Escape Sequence Characters

| Escape Character | Meaning |
|---|---|
| `\n` | New Line |
| `\t` | Tab Space |
| `\"` | Double Quote |

## Example

```python
print("Hello\nWorld")
```

---

# f-String

Modern way to format strings.

```python
name = "Deep"
age = 20

print(f"My name is {name} and age is {age}")
```

---

# Taking String Input

```python
name = input("Enter your name: ")

print(name)
```

---

# Important Points

- Strings are immutable
- Indexing starts from `0`
- Slicing extracts part of string
- Many built-in functions are available
- f-strings make formatting easy