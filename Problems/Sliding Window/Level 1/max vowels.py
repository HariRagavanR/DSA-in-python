s = "abciiidef"
k = 3

def max_vowels(s,k):
    vowels = set('aeiou')
    left = 0
    max_cnt = 0
    vowels_cnt = 0

    for right in range(len(s)):

        if s[right] in vowels:
            vowels_cnt +=1

        if right - left +1 == k:
            max_cnt = max(max_cnt,vowels_cnt)

            if s[left] in vowels:
                vowels_cnt -=1

            left +=1

    return f"Maximum Vowel is {max_cnt}"

print(max_vowels(s,k))

