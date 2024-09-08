class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m * n) != len(original):
            return []
        matrix = [[] for _ in range(m)]
        i = 0
        print(matrix)
        counter = 0
        while i < m:
            j = 0
            while j < n:
                matrix[i].append(original[counter])
                counter += 1
                j += 1 
            i += 1
        return matrix
# Time Complexity O(n * m)
# Space Complexity O(n * m)