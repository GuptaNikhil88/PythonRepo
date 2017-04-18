def anti_vowel(text):
    text1= ""
    vowels = set("aeiouAEIOU")
    for char in text:
        if(char in vowels):
            text1 = text1
        else:
            text1 = text1 + char
    return text1