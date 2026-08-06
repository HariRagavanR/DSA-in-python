s = "car"
t = "rat"

freq = {}

def is_anagram(s,t):
    if len(s) != len(t):
        return False
        
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1

    for ch in t:
        freq[ch] = freq.get(ch,0) - 1

    for value in freq.values():
        if value != 0:
            return False

    return True


print(is_anagram(s,t))