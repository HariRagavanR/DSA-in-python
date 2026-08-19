s = "AABABBA"
k = 1

def char_rep(s,k):

    count = {}
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):

        char = s[right]

        count[char] = count.get(char, 0) +1

        max_freq = max(max_freq, count[char])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -=1
            left +=1

        win_len = right - left +1

        max_len = max(max_len,win_len)

    return max_len

print(char_rep(s,k))

