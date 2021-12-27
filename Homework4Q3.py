# Ryan Franco
# CS610 Homework 4 Question 3

def mergeinterval (interval, newinterval):
    merged = []
    if len(interval) == 0:
        merged.append(newinterval)
    elif len(interval) == 1:
        merged.append(interval[0])
        if merged[0][0] <= newinterval[0] <= merged [-1][1] or newinterval[0] <= merged [-1][0] <= newinterval[1]:
            merged[-1][0] = min(merged[-1][0], newinterval[0])
            merged[-1][1] = max(merged[-1][1], newinterval[1])
        else:
            merged.append(newinterval)
    else:
        found = False
        merged.append(interval[0])
        for i in range(1, len(interval)):
                if not found:
                    if merged[-1][0] <= newinterval[0] <= merged[-1][1] or newinterval[0] <= merged[-1][0] <= newinterval[1]:
                        merged[-1][0] = min(merged[-1][0], newinterval[0])
                        merged[-1][1] = max(merged[-1][1], newinterval[1])
                        found = True
                    else:
                        merged.append(interval[i])
                        i += 1
                else:
                    if merged[-1][0] <= interval[i][0] <= merged[-1][1] or interval[i][0] <= merged[-1][0] <= interval[i][1]:
                        merged[-1][0] = min(merged[-1][0], interval[i][0])
                        merged[-1][1] = max(merged[-1][1], interval[i][1])
                    else:
                        merged.append(interval[i])
                        i += 1
        if not found:
                if merged[-1][0] <= newinterval[0] <= merged[-1][1] or newinterval[0] <= merged[-1][0] <= newinterval[1]:
                    merged[-1][0] = min(merged[-1][0], newinterval[0])
                    merged[-1][1] = max(merged[-1][1], newinterval[1])
                else:
                    merged.append(newinterval)
            
    return merged
interval1 = [[1,3], [6,9]]
newinterval1 = [2,5]
print(mergeinterval(interval1, newinterval1))
interval2 =  [[1,2],[3,5],[6,7],[8,10],[12,16]]
newinterval2 = [4,8]
print(mergeinterval(interval2, newinterval2))
interval3 = []
newinterval3 = [5,7]
print(mergeinterval(interval3, newinterval3))
interval4 = [[1,5]]
newinterval4 = [2,3]
print(mergeinterval(interval4, newinterval4))
interval5 = [[1,5]]
newinterval5 = [2,7]
print(mergeinterval(interval5, newinterval5))

