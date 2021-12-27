
## Homework 2
# Question 3
def sub(s, i):
    target = 0
    for j in range(len(s) - 1):
        goal = 1
        onechar = True
        for k in range (j+1, len(s)):
          if (goal == i):
            onechar = False
          list = [s[j]]
          if s[j] == s[k]:
              continue             
          elif onechar:
              list.append(s[k])
              goal=goal+1
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

print (sub('eceba', 2))
print (sub('aa', 1))