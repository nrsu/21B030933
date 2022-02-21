def palindrome():
    strupd=strng[::-1]
    if strng==strupd:
        return "palindrome"
    else:
        return "not palindrome"
strng=str(input())
print(palindrome())