"""
LeetCode 875. Koko Eating Bananas

Key Idea:-
    Use Binary Search on the Answer to find the minimum eating speed k that allows Koko to finish all bananas within h hours.
    Instead of trying every possible speed from 1 to max(piles), binary search efficiently narrows down the answer.
    For a given speed k:
                        hours=∑⌈kpile⌉
    If hours <= h, Koko can finish → try a smaller speed.
    If hours > h, Koko cannot finish → need a larger speed.

Approach:-
    1.Set the search range:
        l = 1
        r = max(piles)
    2.For each possible middle speed k:
        Calculate the total hours required to eat all bananas.
    3.If the required hours are within h:
        Store k as a possible answer.
        Search for an even smaller speed.
    4.Otherwise:
        Increase the eating speed.
    5.Return the smallest valid speed.
"""
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                # Equivalent to ceil(p / k)
                hours += (p + k - 1) // k

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

"""
Time Complexity:-
                O(n log M)
Space Complexity:-
                O(1)
"""