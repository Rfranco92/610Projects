# Ryan Franco
# CS610 Homework 3 Question 2

def stringgaram (s, t):
    if (len(s) != len(t)):
        return False
    s = sorted(s)
    t = sorted(t)
    for x in range(len(s)):
        if s[x] != t[x]:
            return False
    return True
string1A = 'anagram'
string1B = 'nagaram'
print(stringgaram(string1A, string1B))
string2A = 'rat'
string2B = 'car'
print(stringgaram(string2A, string2B))    
