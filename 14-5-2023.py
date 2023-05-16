# Question 6: How many steps are needed to disconnect the string? 

import collections

def howManySteps(string):

    
    res = 0
    c = 0

    while string:

        # First, we compress string by removing adjacent same characters
        compressed = [string[0]]

        for s in string[1:]:
            if s != compressed[-1]:
                compressed.append(s)
        compressed = ''.join(compressed)

        counter = collections.Counter(compressed)
        mn, min_char = float("inf"), None
        for ch in counter:
            if counter[ch] < mn:
                mn = counter[ch]
                min_char = ch
        
        # Then remove the character with minumum occurences each iteration
        new_string = []
        for ch in compressed:
            if ch != min_char:
                new_string.append(ch)
            else:
                res += 1
        string = ''.join(new_string)
    return res
        
            
    
# 2
print(howManySteps('aabbaa'))

# 92
print(howManySteps('kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor'))