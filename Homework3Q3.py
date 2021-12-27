# Ryan Franco
# CS610 Homework 3 Question 3

def arraysearch (nums, target):
    lefttree = 0
    righttree = len(nums)-1
    while lefttree <= righttree:
        mid=(lefttree+righttree)//2
        if nums[mid]== target:
            return mid
        if nums[mid] < target:
            lefttree = mid+1
        else:
            righttree = mid-1
    return lefttree

numS = [1,3,5,6]
print(arraysearch(numS, 5))
print(arraysearch(numS, 2))
print(arraysearch(numS, 7))
print(arraysearch(numS, 0))
