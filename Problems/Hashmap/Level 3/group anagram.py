strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def grp_anag(strs):
    grp = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in grp:
            grp[key] = []

        grp[key].append(word)

    return list(grp.values())

print(grp_anag(strs))

