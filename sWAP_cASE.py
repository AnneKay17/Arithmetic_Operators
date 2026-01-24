def swap_case(s):
    swappedCase = ""
    for chars in s:
        if chars.isupper():
            swappedCase += chars.lower()
        else:
            swappedCase += chars.upper()
    return swappedCase

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)