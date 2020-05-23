# -*- coding: utf-8 -*-
"""
Created on Sat May 23 07:32:26 2020

@author: Aniket Maity
"""


'''
Given two vessels, one of which can accommodate a liters of water and the other which can accommodate b liters of water, determine the number of steps required to obtain exactly c liters of water in one of the vessels.

At the beginning both vessels are empty. The following operations are counted as 'steps':

emptying a vessel,
filling a vessel,
pouring water from one vessel to the other, without spilling, until one of the vessels is either full or empty.
Input
An integer t, 1<=t<=100, denoting the number of test cases, followed by t sets of input data, each consisting of three positive integers a (the number of liters the first container can hold), b (the number of liters the second container can hold), and c (the final amount of liters of water one vessel should contain), not larger than 40000, given in separate lines.

Output
For each set of input data, output the minimum number of steps required to obtain c liters, or -1 if this is impossible.

Example
Sample input:
2
5
2
3
2
3
4
Sample output:
2
-1
'''
def minNumber(a,b):
    if(a<b):
        return a
    else:
        return b

def gcd(a,b):
    if(b==0):
        return a
    return gcd(b, a%b)




def pour(A,B,C):
    move = 1
    a = A
    b = 0
    tfr = 0
    while(a != C and b !=C):
        tfr = min(a,B-b)
        b+=tfr
        a-=tfr
        move+=1
        if(a == C or b==C):
            break
        if (a==0):
            a = A
            move+=1
        if (b == B):
            b = 0
            move+=1
    return move

def main():
    N = int(input())
    while(N>0):
        N-=1
        a = int(input())
        b = int(input())
        c = int(input())
        if(a<c and b<c):
            print(-1)
        elif (c % gcd(a, b) != 0):
          print("-1\n");
        elif (c == a or c == b):
          print("1\n");
        else:
          print(minNumber(pour(a, b, c), pour(b, a, c)));



    
if __name__== '__main__':
    try:
        main()
    except:
        pass




    