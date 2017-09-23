#!/bin/python

import sys

if __name__ == "__main__":
    
    draws = 0
    arks = 0
    knaves = 0
    
    games = int(raw_input().strip())
    for a0 in xrange(games):
        black, white = raw_input().strip().split(' ')
        black, white = [int(black), int(white)]
        
        p = black + white # piece
        if((p % 4 == 0 and p % 2 == 0) or (p % 4 != 0 and p % 2 != 0 )):
            draws += 1
        
        elif(p % 4 == 0):
            knaves += 1
        
        else:
            arks += 1
       
    print"Draws:", draws
    print"Ark Won:", arks
    print"Knave Won:" ,knaves

