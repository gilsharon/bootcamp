def mean(myLst):
    ''' calculate the mean of a list '''
    return sum(myLst)/ len(myLst)

def median(myLst):
    ''' calculate the mean'''
    sortedList = sorted (myLst)
    return sortedList[len(sortedList)//2]
