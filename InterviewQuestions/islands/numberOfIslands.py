# Easy
# Passes all test cases
class Solution:

    def countIslands(self,matrix):
        count = 0
        rows, cols = len(matrix), len(matrix[0])

        def dfs(row, col):
            if row < 0 or col < 0 or \
            row >= rows or col >= cols or \
            matrix[row][col] == 0:
                return
            
            matrix[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    dfs(row, col)
                    count+=1

        return count

                

                    

                    
