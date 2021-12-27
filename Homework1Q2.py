
##Question 2
def sub(s):
    target = 0
    onechar = True
    for j in range(len(s) - 1):
        onechar = True
        for  k in range (j+1, len(s)):
          if s[j] == s[k]:
              continue             
          elif onechar:
              list = [s[j], s[k]]
              onechar=False 
          else:
            if s[k] in list and k < len(s)-1:
                continue
            else: 
                type = k - j 
                if k == len(s)-1:
                    type = type+1 
                if(type > target):
                    target = type
                break

    return target 

print (sub('eceba'))
print (sub('ccaabbb'))