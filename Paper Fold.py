'''       QUESTION:

Paper Fold :

A piece of paper cannot be folded into half more than 7 times with bare hands. 
So to overcome this, the company RelearnPro has designed a machine to fold the paper as many times you want by generating immense force.

So given a piece of paper with a thickness 'T' mm, and after folding the paper into half  for 'N' times, find what will be size of the paper in mm.

Input Format : Two spaced integers T and N where T is the thickness of the paper in mm and N is the number of times a paper has to be folded into half.

Input Constraints : 1<=T,N<=10^9

Output Format : Print the answer in modulus of 10^9

Sample Input :
1 1

Sample Output :
2














HINTS:

1 - Every time you fold a paper the thickness doubles itself.

2 - 2 power of N

3 - Bitwise operator

'''
























































# ANSWER:

m = 10**9 
def powe(n,a):
    res = 1
    while(a!=0):    
        if(a&1):
            res = (res*n)%m
        a = (a>>1)
        n = (n*n)%m
    return res
thick,fold =map(int,input().split())
print(powe(2,fold)*thick%10**9)
