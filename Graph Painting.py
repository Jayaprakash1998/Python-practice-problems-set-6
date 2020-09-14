'''       QUESTION:

Graph Painting :

Suriya went to a museum where she saw a collection of paintings. She was very much inspired by one of the mountain paintings and decided to draw a mountain. 
So she asked her sister (doing her 10th standard) for a paper. She gave her a bundle of graph sheets and told her not to disturb. 
So Suriya decided to draw mountains by plotting n points. She also wonders how many mountains would be formed with the combinations of those n points. 
The combinations which can form a peek are taken into consideration.

For example, the input is 3, so the numbers 1,2,3 can be arranged in 6 different ways.

1 2 3


1 3 2


2 1 3


2 3 1


3 1 2


3 2 1


In these only 1 3 2 and 2 3 1 looks like forming a mountain peak. 
The numbers are said to form a peak if the values are in increasing order and at one point it should start decreasing till the last number.

The number cannot increase, decrease then again increase, in that case, it is considered to be invalid.

Input Format : The first line consists of single integer N
The Second line consists of N space separated integers

Input Constraints : 1<=N<=10^7

Output Format : Single integer N

Sample Input :
3

Sample Output :
2














HINTS:

1 - The maximum number (N) is at the peak.

2 - The numbers before the peak (upward slope) are in increasing order. The numbers after the peak (downward slope) are in decreasing order.

3 - N (peak number) cannot occupy first and last slots in the sequence as the upward slope and downward slope, respectively, would be missing. 
    Hence, N can be in any of the N-2 slots of a sequence (except first and last).

'''





























# ANSWER:

def power(n,a):
    m = 1000000007
    res = 1
    while(a):
        if a&1:
            res = (res*n)%m
        a = a>>1
        n = (n*n)%m
    return res
n = int(input())
print(power(2,n-1)-2)
