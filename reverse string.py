def reverseString(s):

    if len(s) == 1:
        return s[0]
    firstchar = s[0]

    return reverseString(s[1:]) + firstchar

s ="Ankit jadli"
print (reverseString(s))