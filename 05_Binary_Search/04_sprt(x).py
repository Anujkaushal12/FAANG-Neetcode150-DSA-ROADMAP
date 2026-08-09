"""
LeetCode 69. Sqrt(x)

Key Idea:-
    Use Binary Search to find the largest integer m such that:
                                                                m*m ≤ x
    Since the problem asks for the integer square root, we don't need the decimal part. If m * m is smaller than x, m could be the answer, but we continue searching for a potentially larger value.

Approach:-
    1.Set the search range from 0 to x.
    2.Calculate the middle value using:
        m = l + (r - l) // 2
    3.Compare m * m with x:
        If m² > x → m is too large → search left.
        If m² < x → m is valid, but a larger value may exist → store m in res and search right.
        If m² == x → exact square root found → return m.
    4.If the loop ends, res contains the floor of √x.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # Search range from 0 to x
        l, r = 0, x

        # Stores the largest integer whose square is <= x
        res = 0

        # Binary search
        while l <= r:

            # Calculate the middle value
            m = l + ((r - l) // 2)

            # m is too large
            if m * m > x:
                r = m - 1

            # m is a valid candidate, search for a larger value
            elif m * m < x:
                l = m + 1
                res = m

            # Exact square root found
            else:
                return m

        # Return the integer square root
        return res

"""
Time Complexity
            O(log x)
            Binary search reduces the search space by approximately half in every iteration.
Space Complexity
            O(1)
            Only a constant number of variables are used.
"""