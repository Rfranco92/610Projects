# Ryan Franco
# CS610 Homework 4 Question 1

def closeTime(time):
    result = 'none'
    hour, minute = time.split(':')
    current = int(hour) *60 + int(minute)
    for i in range (current +1, current+1441):
        newtime = i %1440
        h = newtime //60, 
        m = newtime % 60
        if len(str(h)) == 2 and len(str(m)) == 2:
            result = str(h)+':'+str(m)
        if set(result) <= set (time):
            break
    return result


time = '19:34'
print(closeTime(time))
time2 = '23:59'
print(closeTime(time2))
