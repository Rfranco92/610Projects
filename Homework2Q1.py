# Ryan Franco
# CS610 Homework 2 Question 1

def shiftzeros(nums):
    countzeros = 0
    zeros = len(nums)
    for i in range (zeros):
        if (nums[i] == 0):
            countzeros=countzeros+1
   
    for x in range (countzeros):
        nums.remove(0)
    zeros = zeros - len(nums)
    for k in range (zeros):
        nums.append(0)

inputA = [0,1,0,3,12]
inputB = [0]
shiftzeros(inputA)
shiftzeros(inputB)
print(inputA)
print(inputB)
            
