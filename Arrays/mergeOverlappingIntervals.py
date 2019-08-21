def merge(intervals):
    # def findOverlap(a,b):
    #     return max(0, min(a[1], b[1]) - max(a[0], b[0]))
    
    # def mergeIntervals(a,b):
    #     return ([min(a[0], b[0]), max(a[1], b[1])])

    # mergedIntervals = []
    # for i in range(len(intervals)):
    #     for j in range(i+1, len(intervals) - 1):
    #         overlap = findOverlap(intervals[i], intervals[j])
    #         if overlap > 0:
    #             print ("Merge: ", intervals[i], intervals[j])
    #             mergedInterval = mergeIntervals(intervals[i], intervals[j])
    #             print(mergedInterval)
    #             # print(i,j)
    #             # del intervals[i]
    #             # del intervals[j-1]
    #             # intervals.insert(0, mergedInterval)
    #             mergedIntervals.append(mergedInterval)
    #         else:
    #             mergedIntervals.append(intervals[j])

    
    # print(mergedIntervals)
    listIntervals = []
    for x in intervals:
        listIntervals.append(list(x))
    intervals = listIntervals
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for current in intervals:
        previous = merged[-1]
        print(previous)
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    print(merged)

    
A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
merge(A)