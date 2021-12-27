# Ryan Franco
# CS610 Homework 4 Question 5
import collections
def permutation (s1, s2):
    if s1 > s2:
        return False
    s1_counter = collections.Counter(s1)
    for i in range(len(s2) - (len(s1)) + 1):
            if collections.Counter(s2[i:i+len(s1)]) == s1_counter:
                return True
    return False
string1 = 'ab'
stringtestA = 'eidbaooo'
stringtestB = 'eidboaoo'
print(permutation(string1, stringtestA))
print(permutation(string1, stringtestB))