def romanToInt(s):
    roman_numerals = {
        "M": 1000, 
        "D": 500, 
        "C": 100, 
        "L": 50, 
        "X": 10, 
        "V": 5, 
        "I": 1
    }
    number = 0
    for i in range(len(s)):
        if (i<len(s)-1 and roman_numerals[s[i]]<roman_numerals[s[i+1]]):
            number-=roman_numerals[s[i]]
        else:
            number+=roman_numerals[s[i]]
    return number


print(romanToInt("MCMXCIV"))