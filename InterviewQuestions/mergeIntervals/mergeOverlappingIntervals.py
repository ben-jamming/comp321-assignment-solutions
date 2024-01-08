# Medium
# Passes all test cases

class Interval:
 def __init__(self, start, end):
   self.start = start
   self.end = end

 def print_interval(self):
   print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
  def merge(self, intervals):
    if len(intervals) < 2:
      return intervals

    mergedIntervals = []
    intervals = sorted(intervals, key = lambda x: x.start) # Sort by interval starts
    # Naive approach
    curr_start = intervals[0].start
    curr_end = intervals[0].end
    for i in range(1, len(intervals)):
      if intervals[i].start > curr_end:
        print(intervals[i])
        mergedIntervals.append([curr_start, curr_end])
        curr_start = intervals[i].start
        curr_end = intervals[i].end
        
      else:
        curr_end = max(curr_end, intervals[i].end)

    if [curr_start, curr_end] not in mergedIntervals:
      mergedIntervals.append([curr_start, curr_end])
    return mergedIntervals
