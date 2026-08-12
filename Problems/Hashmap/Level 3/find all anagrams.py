s = "cbaebabacd"

p = "abc"

def find_anagrams(s, p):

    result = []

    p_freq = {}

    for ch in p:
        p_freq[ch] = p_freq.get(ch, 0) + 1

    window_freq = {}

    left = 0

    for right in range(len(s)):

        window_freq[s[right]] = window_freq.get(s[right], 0) + 1

        if right - left + 1 > len(p):

            old = s[left]

            window_freq[old] -= 1

            if window_freq[old] == 0:
                del window_freq[old]

            left += 1

        if window_freq == p_freq:
            result.append(left)

    return result