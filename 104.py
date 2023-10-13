def change_case(c):
    if c.isalpha():
        if (c >= 'a' and c <= 'z'):
            return chr(ord(c) - 32)
        if (c >= 'A' and c <= 'Z'):
            return chr(ord(c) + 32)
    return c


c = input()
print(change_case(c))
