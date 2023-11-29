def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")
    print()
