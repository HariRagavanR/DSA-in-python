nums = [0,1,0]

def find_max_length(nums):

    first_seen = {0: -1}

    prefix = 0
    longest = 0

    for i, num in enumerate(nums):

        if num == 0:
            prefix -= 1
        else:
            prefix += 1

        if prefix in first_seen:

            length = i - first_seen[prefix]

            longest = max(longest, length)

        else:
            first_seen[prefix] = i

    return longest

print(find_max_length(nums))