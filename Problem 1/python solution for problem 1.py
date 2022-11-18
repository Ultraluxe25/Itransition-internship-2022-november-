from itertools import combinations

def find_longest_substring(strings):
    if len(strings) == 0:
        return ''

    shortest_string_length = min(map(len, strings))
    shortest_strings = [string for string in strings if len(string) == shortest_string_length]

    x = " ".join(shortest_strings)
    shortest_string_parts = [''.join(l) for i in range(len(x), 0, -1) for l in combinations(x, i)]
    # here we concatinate chars in whole words from list of tuples in one common list
    for element in shortest_string_parts:
        if all(map(lambda string: element in string, strings)):
            return element

    return ''


words = input().split()  # makes list from strings
print(find_longest_substring(words))

# tests for checking the code
'''
ABCDEFZ WBCDXYZ
BCD

132 12332 12312
1

ABCDEFGH ABCDEFG ABCEDF ABCED
ABC

node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE
ABCDE

node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE EDCBA
A

node lcs.js ABCDEFGH ABCDEFG ABCDEF ABCDE EDCBCA
BC

node lcs.js ABCDEFGH ABCDEFG AxBCDEF ABCDxE EDCBCAABCD
BCD

node lcs.js ABCDEFGH 1234


node lcs.js ABCDEFGH
ABCDEFGH
'''
