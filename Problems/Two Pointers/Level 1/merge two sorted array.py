a = [1,3,5]
b = [2,4,6]

def merge_sorted_arr(a,b):
    i = j = 0

    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i +=1

        else:
            result.append(b[j])
            j +=1

    while i < len(a):
        result.append(a[i])
        i +=1

    while j < len(b):
        result.append(b[j])
        j +=1

    return result

print(merge_sorted_arr(a,b))

