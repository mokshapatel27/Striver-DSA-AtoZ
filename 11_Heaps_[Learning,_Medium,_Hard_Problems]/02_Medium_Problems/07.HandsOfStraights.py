#https://leetcode.com/problems/hand-of-straights/description/
#LEFT

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]
                for i in range(groupSize):
                    if count[card + i] < needed:
                        return False
                    count[card + i] -= needed

        return True
