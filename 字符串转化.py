str = 'iAmYourDay'


def aa(a):
    if a.isupper():
        return '_'+a.lower()

    else:
        return a


new_str = ''.join(list(map(aa, str)))
print(new_str)