def substrCount(n, s):
    count = len(s)

    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1,s)
    count += sum([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2,s)
    count += sum([triangular_number(len(x.group(0))-1) for x in m])

    return count

'''
def substrCount(n, s):
    char_freqs = [(s[0], 1)]
    for i in range(1, len(s)):
        char = s[i]
        if char == char_freqs[-1][0]:
            char_freqs[-1] = (char, char_freqs[-1][1] + 1)
        else:
            char_freqs.append((char, 1))
    print(char_freqs)

    total = 0
    for i in range(0, len(char_freqs)):
        val = char_freqs[i][1]
        # e.g. `(a, 4)`
        if val > 1:
            total += val * (val + 1) / 2
        # e.g. `[(a, 4), (b, 1), (a, 4)]`
        elif i > 0 and i < len(char_freqs) - 1 and val == 1:
            total += 1
            if char_freqs[i-1][0] == char_freqs[i+1][0]:
                total += 1
        else:
            total += 1
                
    print(total)
    return int(total)
'''

n = int(input())
s = input()

result = substrCount(n, s)
print(result)