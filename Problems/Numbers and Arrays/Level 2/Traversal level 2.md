# 📘 CHAPTER 1.2 - Traversal Pattern (Level 2)

---

# 1️⃣ Find First Occurrence

## 📖 Definition

Find the **first position (index)** where the target element appears.

---

## 🎯 Recognition Keywords

```
First
Occurrence
Index
Position
Search
```

---

## 🧠 Algorithm

```
Start

↓

Visit every element from left to right

↓

Current element == Target?

↓

Yes

↓

Return current index

↓

No

↓

Continue

↓

Not Found

↓

Return -1
```

---

## 🐍 Python Template

```python
for i in range(len(arr)):

    if arr[i] == target:
        return i

return -1
```

---

## 💡 Explanation

- Start from index `0`
- Compare each element with target
- As soon as it matches, stop and return the index
- If loop finishes, target doesn't exist

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 2️⃣ Find Last Occurrence

## 📖 Definition

Find the **last position (index)** where the target appears.

---

## 🎯 Recognition Keywords

```
Last
Occurrence
Last Index
```

---

## 🧠 Algorithm

```
Start

↓

last = -1

↓

Traverse entire array

↓

Current == Target?

↓

Yes

↓

Update last = current index

↓

Continue

↓

Return last
```

---

## 🐍 Python Template

```python
last = -1

for i in range(len(arr)):

    if arr[i] == target:
        last = i

return last
```

---

## 💡 Explanation

Don't stop after first match.

Keep updating until traversal finishes.

The final stored index is the last occurrence.

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 3️⃣ Count Positive Numbers

## 📖 Definition

Count how many positive numbers are present.

---

## 🎯 Recognition Keywords

```
Count
Positive
Greater than Zero
```

---

## 🧠 Algorithm

```
count = 0

↓

Visit every element

↓

Element > 0 ?

↓

Yes

↓

count++

↓

Return count
```

---

## 🐍 Python Template

```python
count = 0

for num in arr:

    if num > 0:
        count += 1

return count
```

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 4️⃣ Count Negative Numbers

## 📖 Definition

Count elements smaller than zero.

---

## 🎯 Recognition Keywords

```
Negative

Less than Zero

Count
```

---

## 🐍 Python Template

```python
count = 0

for num in arr:

    if num < 0:
        count += 1

return count
```

---

## 💡 Logic

Only the condition changes.

Positive → `num > 0`

Negative → `num < 0`

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 5️⃣ Count Zeroes

## 📖 Definition

Count how many zeroes exist.

---

## 🎯 Recognition Keywords

```
Zero

Count

Frequency
```

---

## 🐍 Python Template

```python
count = 0

for num in arr:

    if num == 0:
        count += 1

return count
```

---

## 💡 Observation

Positive, Negative and Zero count all use the same Traversal pattern.

Only the condition changes.

---

# 6️⃣ Find Largest Even Number

## 📖 Definition

Find the biggest even number.

---

## 🎯 Recognition Keywords

```
Largest

Maximum

Even
```

---

## 🧠 Algorithm

```
largest = None

↓

Traverse

↓

Is Even?

↓

Yes

↓

Compare

↓

Update

↓

Return largest
```

---

## 🐍 Python Template

```python
largest = None

for num in arr:

    if num % 2 == 0:

        if largest is None or num > largest:
            largest = num

return largest
```

---

## 💡 Explanation

Two checks happen here:

- Is it even?
- Is it larger than current largest?

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 7️⃣ Find Smallest Odd Number

## 📖 Definition

Find the smallest odd number.

---

## 🎯 Recognition Keywords

```
Smallest

Minimum

Odd
```

---

## 🐍 Python Template

```python
smallest = None

for num in arr:

    if num % 2 != 0:

        if smallest is None or num < smallest:
            smallest = num

return smallest
```

---

## 💡 Observation

Same logic as Largest Even.

Only comparison changes.

---

# 8️⃣ Reverse Print

## 📖 Definition

Print elements from last to first.

---

## 🎯 Recognition Keywords

```
Reverse

Print

Backward
```

---

## 🧠 Algorithm

```
Start from last index

↓

Print

↓

Move left

↓

Repeat
```

---

## 🐍 Python Template

```python
for i in range(len(arr)-1, -1, -1):

    print(arr[i])
```

---

## 💡 Explanation

`range(start, stop, step)`

```
start = last index

stop = -1

step = -1
```

---

## ⏱️ Complexity

Time : `O(n)`

Space : `O(1)`

---

# 9️⃣ Replace Element

## 📖 Definition

Replace every occurrence of one value with another.

---

## 🎯 Recognition Keywords

```
Replace

Update

Modify

Change
```

---

## 🐍 Python Template

```python
for i in range(len(arr)):

    if arr[i] == old:

        arr[i] = new
```

---

## 💡 Explanation

Need index because we are modifying the array.

That's why we use

```python
for i in range(len(arr))
```

instead of

```python
for num in arr
```

---

## 🔟 Move Zeroes

## 📖 Definition

Move all zeroes to the end while keeping the order of non-zero elements.

---

## 🎯 Recognition Keywords

```
Move

Shift

Rearrange

Zeroes
```

---

## 🧧 Method 1 (Easy to Understand)

### 🐍 Python Template

```python
result = []

for num in arr:

    if num != 0:
        result.append(num)

while len(result) < len(arr):

    result.append(0)

return result
```

---

## 💡 Explanation

Step 1

Collect all non-zero numbers.

Step 2

Append zeroes until sizes become equal.

---

## 🧧 Method 2 (Interview Optimised)

```python
left = 0

for right in range(len(arr)):

    if arr[right] != 0:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
```

---

## 💡 Explanation

- `right` scans every element.
- `left` marks where the next non-zero should go.
- Whenever a non-zero is found, swap it into the correct position.
- Zeroes naturally move to the end.

---

# 📋 Level 2 Pattern Summary

| Problem | Core Idea |
|----------|-----------|
| First Occurrence | Stop at first match |
| Last Occurrence | Keep updating answer |
| Count Positive | Count if `> 0` |
| Count Negative | Count if `< 0` |
| Count Zeroes | Count if `== 0` |
| Largest Even | Filter + Maximum |
| Smallest Odd | Filter + Minimum |
| Reverse Print | Reverse Traversal |
| Replace Element | Modify using index |
| Move Zeroes | Traverse + Rearrange |

---

# 🎯 Pattern Learning

Notice something?

Most Level 2 questions are still **Traversal**.

The only thing that changes is the **condition inside the loop**.

```
Traversal

↓

Condition

↓

Action
```

Examples:

```
num > 0

↓

Count++
```

```
num % 2 == 0

↓

Compare Maximum
```

```
arr[i] == old

↓

Replace
```

The loop stays almost the same.

Only the condition and action change.

That is the real power of Pattern Thinking.