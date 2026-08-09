"""
LeetCode 374. Guess Number Higher or Lower

Key Idea:-
    Use Binary Search on the range 1 to n.
    The guess() API tells us whether our current guess is:
        1 → our guess is too low, so search the right half.
        -1 → our guess is too high, so search the left half.
        0 → correct number found.

Approach:-
    1.Set the search range:
        l = 1
        r = n
    2.Calculate the middle number.
    3.Call guess(m):
        If res > 0, the picked number is higher → l = m + 1.
        If res < 0, the picked number is lower → r = m - 1.
        If res == 0, return m.
    4.Continue until the number is found.
"""
# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize the search range
        l, r = 1, n

        # Continue until the picked number is found
        while True:
            # Find the middle number
            m = (l + r) // 2

            # Ask the API whether our guess is correct
            res = guess(m)

            # Picked number is higher than our guess
            if res > 0:
                l = m + 1

            # Picked number is lower than our guess
            elif res < 0:
                r = m - 1

            # Correct number found
            else:
                return m
"""
Time Complexity:-
    O(log n)
    Each API call eliminates approximately half of the remaining search range.
Space Complexity:-
    O(1)
    Only l, r, m, and res are used.
"""