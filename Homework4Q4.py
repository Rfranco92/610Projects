# Ryan Franco
# CS610 Homework 4 Question 4
def median(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m = len(nums1)
    n = len(nums2)
    start = 0
    end = m
    while start <= end:
        leftbranch = (start + end) // 2
        rightbranch = (m + n + 1) // 2 - leftbranch
        left = -1000 if leftbranch == 0 else nums1[leftbranch - 1]
        right = 1000 if leftbranch == m else nums1[leftbranch]
        maxleft = -1000 if rightbranch == 0 else nums2[rightbranch - 1]
        minright = 1000 if rightbranch == n else nums2[rightbranch]
        if left <= minright and maxleft <= right:
            if (m + n) % 2 == 0:
                return (max(left, maxleft) + min(right, minright)) / 2
            else:
                return max(left, maxleft)
        elif left > minright:
            end = leftbranch - 1
        else:
            start = leftbranch + 1

numslist1 = [1,3]
numslist1b = [2]
print (median(numslist1, numslist1b))
numslist2 = [1, 2]
numslist2b = [3, 4]
print(median(numslist2, numslist2b))
numslist3 = [0, 0]
numslist3b = [0, 0]
print(median(numslist3, numslist3b))
numslist4 = []
numslist4b = [1]
print(median(numslist4, numslist4b))
numslist5 = [2]
numslist5b = []
print(median(numslist5, numslist5b))