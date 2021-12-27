## Homework 2
# Question 4
import random
def findPeaks (nums):
    totalPeaks = []
    totalNums = len(nums)
    if(nums[0] > nums[1]):
        totalPeaks.append(0)
    for i in range(1, totalNums-1):
        if (nums[i] > nums[i-1] and nums[i] > nums[i+1]):
          totalPeaks.append(i)
    if(nums[totalNums-1] > nums[totalNums-2]):
        totalPeaks.append(totalNums-1)
    
    return random.choice(totalPeaks)
nums1 = [1,2,3,1]
print(findPeaks(nums1))
nums2 = [1,2,1,3,5,6,4]
print(findPeaks(nums2))
