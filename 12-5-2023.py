# Question 5: What do I say when I am decoded?

def decode(encoded, codebook):
    longest = 0
    length = len(encoded)
    

    # The codebook is given as a mapping of character -> code. 
    # Swap the key and value to get the mapping code -> character
    codes = {}
    for k in codebook:
        longest = max(longest, len(codebook[k]))
        codes[codebook[k]] = k
    
    
    result = []

    def decodeString(i, decoded_string):
        nonlocal longest
        nonlocal length
        # If we reach the end of the string, it has been decoded successfully, so we can stop
        if i >= length:
            result.append(decoded_string)
            return
        
        # Loop through the characters coded string and check if substrings match any from the codebook
        for j in range(i+2, min(i+longest, len(encoded))+1):
            substring = encoded[i:j]
            # Once a character matches, we recursively check the rest of the string
            if substring in codes:
                decodeString(j, decoded_string+codes[substring])
                break
    
    decodeString(0, '')
    return result[0]


codebook = {'a': '00',
'b': '01',
'c': '10',
'd': '1100',
'e': '1101',
'f': '1110',
'g': '111100',
'h': '111101',
'i': '111110',
'j': '1111110000',
'k': '1111110001',
'l': '1111110010',
'm': '1111110011',
'n': '1111110100',
'o': '1111110101',
'p': '1111110110',
'q': '1111110111',
'r': '1111111000',
's': '1111111001',
't': '1111111010',
'u': '1111111011',
'v': '1111111100',
'w': '1111111101',
'x': '1111111110',
'y': '1111111111',
'z': '11111111110000',
' ': '11111111110001'}

phrase = '11111011111111110001111111001011111101011111111100110111111111110001001111110100111100110111111100101111010010111111000111111111110001101111110101110011011111111111000110111101001111110010111111001011011111110100111100110111111111110001011101100011111110111111111001110111111111110001111110111111101011111111110001111110111111100111111111110001111011111110111111110100111111111100010011111101001100111111111100011101111111111010111110111111101011111011111101001111001111111111000100111111010011001111111111000111111011111111110001110011111011111110011111110010111110111111000111011111111111000111111110101111011101111111111100011111111101111111010111111110001100111111111100011111111111000111111111110001111111101011110100111111101011111111110001001111110110111111011011010011111110001111111001111111111100011111101111110100111111111100011111111010111101110111111111110001111111011011110111111110000011111110011101'

# iyabloveyabangelhackyabcodeyabchallengeyabbecauseyabityabisyabfunyabandyabexcitingyabandyabiyabdislikeyabtheyabwordyabyabyabthatyabappearsyabinyabtheyabphrase
print(decode(phrase, codebook))


# ANALYSIS
# Time complexity: O(n), where n is the length of the input phrase
# Space complexity: O(1)
        

