'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

use a hash to add all common prefixes if they match then return hash

def longestCommonPrefix(strs: list[str]) -> str:
    hash = {}
    for i in strs:
        for j in strs:
            print(i)
            
        
print(longestCommonPrefix(['Dereck','Duran']))
'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ""
    if len(strs) == 1: return strs[0]
    
    strs.sort()#sorting them
    p = ""#new string for prefix 
    for x, y in zip(strs[0], strs[-1]): #ZIPPED UP AND STRAPPED comparing first to last strings sorted
        if x == y: p+=x 
        else: break
    return p
print(longestCommonPrefix(["Dereck", "Duran"]))