arr = [-1,0,1122221,22,1,0,33,0,0,0,5552,12222,0]

largest = None

for i in arr:
    if i % 2 == 0:

        if largest is None or i > largest:

            largest = i

print(largest)

    