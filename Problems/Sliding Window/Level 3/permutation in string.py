s1 = "ab"
s2 = "eidbaooo"

# Dictionary Version:
def check_inclusion(s1, s2):

    if len(s1) > len(s2):
        return False

    target = {}

    for char in s1:
        target[char] = target.get(char, 0) + 1

    window = {}

    left = 0
    k = len(s1)

    for right in range(len(s2)):

        char = s2[right]

        window[char] = window.get(char, 0) + 1

        if right - left + 1 == k:

            if window == target:
                return True

            left_char = s2[left]

            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            left += 1

    return False
print(check_inclusion(s1,s2))

"""
# Optimized Version:

def check_inclusion(s1, s2):

    if len(s1) > len(s2):
        return False

    target = [0] * 26
    window = [0] * 26

    for char in s1:
        target[ord(char) - ord('a')] += 1

    left = 0

    for right in range(len(s2)):

        window[ord(s2[right]) - ord('a')] += 1

        if right - left + 1 > len(s1):

            window[ord(s2[left]) - ord('a')] -= 1
            left += 1

        if window == target:
            return True

    return False

print(check_inclusion(s1,s2))

"""
