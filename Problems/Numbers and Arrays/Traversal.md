# 📘 DSA Pattern Mastery
> Interview-Oriented DSA Notes using Python

---

# Chapter 1 - Traversal Pattern

## 📖 What is Traversal?

Traversal means visiting **every element exactly once** and processing it.

> **Definition**
>
> Visit every element in the array one by one.

---

# 🎯 Purpose

Traversal is used when we need to process every element.

Examples:

- Find Maximum
- Find Minimum
- Count Elements
- Sum
- Search
- Replace
- Update

---

# 🔍 Pattern Recognition

If the question contains these keywords,

```
Find
Count
Maximum
Minimum
Search
Print
Replace
Update
Compare
Exists
```

➡️ First think about **Traversal Pattern**.

---

# 🧠 Algorithm

```
Start

↓

Visit first element

↓

Process element

↓

Visit next element

↓

Repeat

↓

Return Answer
```

---

# 🐍 Python Template 1

### Traverse using Elements

```python
for num in arr:
    # Process num
```

### Explanation

- `num` → Current element
- Automatically visits every element
- No index available

### Use Cases

- Sum
- Count
- Maximum
- Minimum
- Average

---

# 🐍 Python Template 2

### Traverse using Index

```python
for i in range(len(arr)):
    # Process arr[i]
```

### Explanation

- `i` → Current Index
- `arr[i]` → Current Element

### Use Cases

- Find Index
- Replace Values
- Update Array

---

# 🐍 Template 3

## Find Maximum Element

```python
maximum = arr[0]

for num in arr:

    if num > maximum:
        maximum = num

return maximum
```

### Algorithm

```
Take first element as maximum

↓

Compare every element

↓

Current > Maximum?

↓

Yes

↓

Update Maximum

↓

Return Maximum
```

Time Complexity

```
O(n)
```

Space Complexity

```
O(1)
```

---

# 🐍 Template 4

## Find Minimum Element

```python
minimum = arr[0]

for num in arr:

    if num < minimum:
        minimum = num

return minimum
```

---

# 🐍 Template 5

## Sum of Array

```python
total = 0

for num in arr:

    total += num

return total
```

---

# 🐍 Template 6

## Count Elements

```python
count = 0

for num in arr:

    count += 1

return count
```

---

# 🐍 Template 7

## Count Even Numbers

```python
count = 0

for num in arr:

    if num % 2 == 0:
        count += 1

return count
```

---

# 🐍 Template 8

## Linear Search

```python
for i in range(len(arr)):

    if arr[i] == target:

        return i

return -1
```

### Algorithm

```
Visit every element

↓

Found?

↓

Yes

↓

Return Index

↓

No

↓

Continue

↓

Return -1
```

---

# 🐍 Template 9

## Replace Element

```python
for i in range(len(arr)):

    if arr[i] == old:

        arr[i] = new
```

---

# 🐍 Template 10

## Move Zeroes (Basic Traversal)

```python
result = []

for num in arr:

    if num != 0:

        result.append(num)

while len(result) < len(arr):

    result.append(0)
```

---

# 📚 Core Problems (Must Master)

- Print Array
- Sum of Array
- Find Maximum
- Find Minimum
- Count Elements
- Count Even Numbers
- Count Odd Numbers
- Linear Search
- Check Element Exists

---

# 📚 Pattern Building Problems

- Find First Occurrence
- Find Last Occurrence
- Count Positive Numbers
- Count Negative Numbers
- Count Zeroes
- Largest Even Number
- Smallest Odd Number
- Replace Element
- Reverse Print
- Move Zeroes

---

# 📚 Interview Level Problems

- Best Time to Buy and Sell Stock
- Product of Array Except Self
- Majority Element
- Pivot Index
- Maximum Consecutive Ones
- Find Missing Number
- Second Largest
- Maximum Difference

---

# ⚠️ Common Mistakes

### ❌ Nested Loop

```python
for i in arr:
    for j in arr:
```

Time Complexity

```
O(n²)
```

Usually unnecessary.

---

### ❌ Wrong Initialization

Wrong

```python
maximum = 0
```

Correct

```python
maximum = arr[0]
```

---

### ❌ Returning inside Loop

Wrong

```python
for num in arr:
    return num
```

Returns only the first element.

---

# 📋 Traversal Cheat Sheet

| Property | Value |
|----------|-------|
| Pattern | Traversal |
| Purpose | Visit every element |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

---

## Recognition Keywords

```
Find
Count
Maximum
Minimum
Search
Print
Replace
Update
Compare
Exists
```

---

## Templates

```python
for num in arr:
```

```python
for i in range(len(arr)):
```

---

# 📝 Practice Order

```
1. Print Array

2. Sum of Array

3. Find Maximum

4. Find Minimum

5. Count Even Numbers

6. Linear Search

7. Find First Occurrence

8. Find Last Occurrence

9. Move Zeroes

10. Best Time to Buy and Sell Stock
```

---

# 💡 Interview Mindset

Whenever you read a question,

```
Question

↓

Find Keywords

↓

Traversal?

↓

Design Algorithm

↓

Dry Run

↓

Python Template

↓

Customize Logic

↓

Return Answer
```

---

# 🎯 Goal

Don't memorize solutions.

Understand the pattern.

Once you master the Traversal Pattern,

you should be able to solve any Traversal-based problem with confidence.