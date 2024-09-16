class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        def convert(time: str):
            hours = int(time[0:2])
            mins = int(time[3:])
            total_mins = hours * 60 + mins
            return total_mins
        minimum_mins = float('inf')
        for r in range(len(timePoints) - 1):
            x = abs(convert(timePoints[r+1]) - convert(timePoints[r]))
            y = 24 * 60 - x
            z = min(x, y)
            print(x, y, z)
            minimum_mins = min(minimum_mins, z)
        x = abs(convert(timePoints[0]) - convert(timePoints[-1]))
        y = 24 * 60 - x
        z = min(x,y)
        minimum_mins = min(minimum_mins, z)
        return minimum_mins