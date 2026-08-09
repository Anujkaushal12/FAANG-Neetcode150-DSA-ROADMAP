"""
LeetCode 74. Search a 2D Matrix

Key Idea:-
    Use Binary Search twice:
    First, perform binary search on the rows to identify which row could contain the target.
    Then perform binary search within that row to find the target.
    This works because:
        Each row is sorted.
        The first element of each row is greater than the last element of the previous row.

Approach"-
    Step 1 — Find the Correct Row
    Use top and bot to perform binary search on the rows.
    
    For the middle row:
        If target > matrix[row][-1] → target must be below → top = row + 1.
        If target < matrix[row][0] → target must be above → bot = row - 1.
        Otherwise, the target could be inside this row → stop row search.
    
    Step 2 — Binary Search Inside the Row
    Once the correct row is identified:
        Set l = 0 and r = Cols - 1.
        Compare target with the middle element.
        Move left or right accordingly.
        Return True if found, otherwise False.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Get number of rows and columns
        Rows, Cols = len(matrix), len(matrix[0])

        # Binary search to find the possible row
        top, bot = 0, Rows - 1

        while top <= bot:
            # Find the middle row
            row = (top + bot) // 2

            # Target is greater than the last element
            # of this row, so search lower rows
            if target > matrix[row][-1]:
                top = row + 1

            # Target is smaller than the first element
            # of this row, so search upper rows
            elif target < matrix[row][0]:
                bot = row - 1

            else:
                # Target could exist in this row
                break

        # No valid row was found
        if not (top <= bot):
            return False

        # The candidate row
        row = (top + bot) // 2

        # Binary search within the selected row
        l, r = 0, Cols - 1

        while l <= r:
            # Find the middle column
            m = (l + r) // 2

            # Target is greater, search right half
            if target > matrix[row][m]:
                l = m + 1

            # Target is smaller, search left half
            elif target < matrix[row][m]:
                r = m - 1

            # Target found
            else:
                return True

        # Target does not exist
        return False

"""
Time Complexity:-
                O(log m + log n)

Space Complexity:-
                O(1)
"""