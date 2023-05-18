# Question 6: How many steps are needed to disconnect the string? 

import collections

def howManySteps(string):

    
    result = 0

    while string:

        # Notice that given a string `aaabbaa`, we get the same result as if given the string `aba`
        # So, we can make this tasks easier if we "compress" a string by removing adjacent same characters
        compressed = [string[0]]
        for s in string[1:]:
            if s != compressed[-1]:
                compressed.append(s)
        compressed = ''.join(compressed)

        # Ceate a dictionary giving the counts of each character
        counter = collections.Counter(compressed)
        mn, min_char = float("inf"), None
        for ch in counter:
            # Get the character with the lowest count
            if counter[ch] < mn:
                mn = counter[ch]
                min_char = ch
        
        # Then remove the character with minumum count/occurence in each iteration
        new_string = []
        for ch in compressed:
            if ch != min_char:
                new_string.append(ch)
            else:
                result += 1
        string = ''.join(new_string)
    return result
        
            
    
# 2
print(howManySteps('aabbaa'))

# 92
print(howManySteps('kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor'))

# ANALYSIS
# Time complexity: O(n**2), where n is the length of the input string. 
# Space complexity: O(n), since we create a new string and dictionary