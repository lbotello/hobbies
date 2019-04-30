import string

def is_pangram(s):
    used = []
    used_lett = 0

    for lett in s:
        if not lett.isalpha():
            continue
        if lett not in used:
            used.append(lett.lower())
            used_lett += 1
    if used_lett == 26:
        return True
    else:
        return False

print "The quick, brown fox jumps over the lazy dog!"
print 'Pangram : '
print is_pangram("The quick, brown fox jumps over the lazy dog!")
"""
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
