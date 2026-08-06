arr = [1, 2, 3, 4, 6]

n = max(arr)

expected = n * (n+1) // 2

actual = sum(arr)

print(expected - actual)