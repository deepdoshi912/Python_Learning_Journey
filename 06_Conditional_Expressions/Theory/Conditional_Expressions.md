# Conditional Expressions in Python

Conditional expressions are used to make decisions in a program.

They allow Python to execute different blocks of code based on conditions.

---

# if Statement

The `if` statement executes code only when the condition is True.

## Syntax

```python
if condition:
    # code
```

## Example

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
```

---

# if-else Statement

Used when there are two possible outcomes.

## Syntax

```python
if condition:
    # code
else:
    # code
```

## Example

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
```

---

# if-elif-else Statement

Used when there are multiple conditions.

## Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

# Nested if Statement

An `if` statement inside another `if` statement.

## Example

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
```

---

# Comparison Operators

Used in conditions.

| Operator | Meaning |
|----------|----------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

## Example

```python
a = 10
b = 20

if b > a:
    print("b is greater")
```

---

# Logical Operators

Used to combine conditions.

| Operator | Meaning |
|----------|----------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the condition |

## Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

# Ternary Operator

Short form of if-else.

## Syntax

```python
value_if_true if condition else value_if_false
```

## Example

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

# User Input with Conditions

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# Important Points

- `if` checks a condition.
- `else` runs when condition is False.
- `elif` is used for multiple conditions.
- Conditions return either True or False.
- Indentation is very important in Python.