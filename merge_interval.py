class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if (len(intervals) > 2):
            for lst in intervals:
                for lst1 in intervals:
                    a = lst[0]
                    b = lst1[0]
                    c = lst[1]
                    d = lst1[1]
                    if((a+1 == b or c == b) and (c < d or c == d)):
                        if(lst in intervals):
                            intervals.remove(lst)
                        if(lst1 in intervals):
                            intervals.remove(lst1)
                        intervals.append([lst[0], lst1[1]])
            return intervals
        elif (len(intervals)==2):
             if (intervals[0]== intervals[1]):
                return [intervals[0]]
        
             else:
                 a = intervals[0][0]
                 b = intervals[1][0]
                 c = intervals[0][1]
                 d = intervals[1][1]
                 if (b!=0):
                     if ((a < b or a == b) and (c < d or c == d) and ( b <= c)):
                        if([a,c] in intervals):
                            intervals.remove([a,c])
                        if([b,d] in intervals):
                            intervals.remove([b,d])
                        intervals.append([a, d])
                     return intervals
                 else:
                      return [intervals[1]] if (c < d) else [[b,c]]
        elif (len(intervals)==1):
            return intervals
                    
            
