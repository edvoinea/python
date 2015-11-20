from collections import Counter


# to be backwards compatible with the old Python 2.X
def decode_if_needed(string):
    try:
        return string.decode('utf-8')
    except AttributeError:
        return string


def word_count(text):
    replace_nonalpha = lambda c: c.lower() if c.isalnum() else ' '
    text = ''.join(replace_nonalpha(c) for c in decode_if_needed(text))
    return Counter(text.split())
