strs = "hari"

def rev_str(strs):

    strs = list(strs)

    left = 0
    right = len(strs) - 1

    while left < right:
        strs[left],strs[right] = strs[right],strs[left]

        left +=1
        right -=1

    return "".join(strs)

print(rev_str(strs))
