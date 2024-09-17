class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def helper(item):
            return (item[0], item[1])
        intervals.sort(key=helper)
        output = [intervals[0]]
        i = 1
        while i < len(intervals):
            if output[-1][-1] >= intervals[i][0]:
                merged = output.pop()
                merged[-1] = max(intervals[i][-1], merged[-1])
                output.append(merged)
            else:
                output.append(intervals[i])
            i += 1
        return output
# Time complexity O(n log n)
# Space complexity O(n)