arr = [10,22,1,33,555,2222]

# average = total_sum / total count of num

sum = count = 0
# count = 0
for i in arr:
    sum = sum + i

    count = count + 1

    average = sum / count


print([average])