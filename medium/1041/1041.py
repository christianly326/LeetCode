class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0, 0]
        table = {
            'North': ('West', 'East'),
            'South': ('East', 'West'),
            'East': ('North', 'South'),
            'West': ('South', 'North')
        }
        change = {
            'North': (1, 1),
            'South': (-1, 1),
            'East': (1, 0),
            'West': (-1, 0)
        }
        face = 'North'
        for n in instructions:
            if n == 'L':
                face = table[face][0]
            elif n == 'R':
                face = table[face][1]
            else:
                position[change[face][1]] += change[face][0]
                has_changed = True
        
        return position == [0, 0] or face != 'North' 
# Time Complexity O(n)
# Space Complexity O(1)