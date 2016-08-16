# -*- coding: utf-8 -*-

def calculateHandlen(hand):
    count = 0
    for i in hand:
        count += hand[i]
    return count
    
hand = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}    
print calculateHandlen(hand)