def string(haystack,needle):
    char = needle[0]
    count = len(needle)
    for i in range(len(haystack)):
        if needle in haystack:
            if haystack[i] == char:
                if haystack[i:i+count] == needle:
                    return i
    return -1

