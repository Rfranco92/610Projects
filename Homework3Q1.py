# Ryan Franco
# CS610 Homework 3 Question 1

def stringcomparer (S, T):
    splitS = list(S)
    splitT = list(T)
    if (len(S) == len(T)-1):
        for x in S:
            splitT.remove(x)
        if(len(splitT) == 1):
            return True
        else:
            return False
    elif (len(S) == len(T)):
        if (S == T):
            return False
        for x in T:
            splitS.remove(x)
        if(len(splitS) == 1):
            return True
        else:
            return False
    elif (len(S) == len(T)+1):
        for x in T:
            splitS.remove(x)
        if(len(splitS) == 1):
            return True
        else:
            return False
    else:
        return False

string1A = 'ab'
string1B = 'acb'
print(stringcomparer(string1A, string1B))
string2A = ''
string2B = ''
print(stringcomparer(string2A, string2B))
string3A = ''
string3B = 'A'
print(stringcomparer(string3A, string3B))