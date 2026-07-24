arr = [10,22,1,33,555,2222]

target = 22

current_index = 0

found = -1

for i in arr:

    if i == target:
        found = current_index
        break

    current_index = current_index + 1 #Linear Searching by moving the index position 0 --> 1 .... 2 .... 3 ..... until it's found

print(current_index)
