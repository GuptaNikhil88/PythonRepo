def reverse(text):
    text1 =""
    tlen = len(text)
    for i in range(0,tlen):
        text1 = text1 + text[tlen-i-1]
    return text1
        