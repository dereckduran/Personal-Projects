def isIsomorphic(s: str,t: str) -> bool:
    if not s:
        return False
    if len(s) != len(t):
        return False
    hash = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        if c1 in hash:
            if hash[c1] != c2:
                return False
            else:
                hash[c1] = c2
    return True

print(isIsomorphic('foo', 'bar'))