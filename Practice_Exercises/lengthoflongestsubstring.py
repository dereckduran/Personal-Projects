def lengthOfLongestSubstring(s: str) -> int:
      
    hash = {}
    #seen = []
    maxlength = start = 0 #was missing starting value
    #split = s.split()
    #for i in range(len(split)):didnt need to append
        #hash.append(i)
    
    for i,value in enumerate(s):#couldve used enumerate 
        
        if value in hash:#right thinking wrong variables
            counter = hash[value]+ 1
            if counter > start:
                start = counter
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        hash[value] = i
    return maxlength
    
print(lengthOfLongestSubstring("Dereck"))