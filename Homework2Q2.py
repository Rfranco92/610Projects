# Ryan Franco
# CS610 Homework 2 Question 2

def findnumber (numlist):
    count = 0
    numlist.sort()
    for i in range (len(numlist)):
        if (count==numlist[i]):
            count=count+1
        else:
            return count

nums1 = [3,0,1]
nums2 = [9,6,4,2,3,5,7,0,1]

print(findnumber(nums1))
print(findnumber(nums2))