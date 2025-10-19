
def isValid(s: str) -> bool:
    stack = []
    dict = {'}':'{', ')':'(', ']':'['}
    for char in s:
        if char in dict.values():
            print(char)
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

print(isValid('()'))