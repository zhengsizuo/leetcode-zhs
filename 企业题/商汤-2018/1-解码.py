import functools
@functools.lru_cache(None)
def decode(num_str):
    if not num_str: return 1
    if len(num_str)==1: return 1 if num_str[0]!='0' else 0

    if int(num_str[0]) > 2:
        return decode(num_str[1:])
    else:
        return decode(num_str[1:]) + decode(num_str[2:])


import functools
@functools.lru_cache(None)
def numDecodings(s: str):
    if s[0] == '0': return 0

    if len(s) == 1:
        return 1 if s[0] != '0' else 0
    if len(s) == 2:
        if s[-1] != '0':
            return 2 if int(s) <= 26 else 1
        else:
            return 1 if 0 < int(s[0]) <= 2 else 0

    if int(s[0]) > 2:
        return numDecodings(s[1:])

    else:
        if 1 <= int(s[:2]) <= 26:
            return numDecodings(s[1:]) + numDecodings(s[2:])
        else:
            return numDecodings(s[1:])

# num_str = '31717126241541717'
num_str = input()
print(decode(num_str))
