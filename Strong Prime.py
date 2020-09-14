'''       QUESTION:

Strong Prime :

You are given Q queries and in each query. 
There are two numbers L and R you have to calculate the number of strong primes present in the range L and R inclusive.

Note : A strong prime is a prime number that is greater than the arithmetic mean of the nearest prime above and below. 
Algebraically,a prime p said to be strong if

2pn > pn-1 + pn+1

Where n is their index in the ordered set of prime numbers, where pi denotes the ith .ptime

Input Format : The first line of the input contains an integers Q denotes the numbers of queries
Then Q lines follow each containing two numbers L and R

Input Constraints : 1<= Q <= 10^5
1<= L <= R <= 10^5

Output Format : For each query print the number of strong primes present in the range L to R inclusively
The answer to each test case should come in new line.

Sample Input :
3
10  20
20  30
30  50

Sample Output :
2
1
2















HINTS:

1 - What if all the 10^5 queries are 1 and 10^5.

2 - Precompute the primes using the Sieve method. and store the primes in a separate list.

3 - From the computed primes, mark the primes that satisfies the condition and construct a prefix array from 0 to 10^5 and answer each query in O(1) time complexity.

'''










































# ANSWER:

from math import sqrt
def sieve():
	primes=[]
	n = 100004 #100003 is prime
	#n=50 #trial
	lmts = int(sqrt(n))+1
	l=[True for i in range(n)]
	strong=[]
	scount=[0,0]
	s=0
	for i in range(2,n):
		scount.append(s)
		if l[i]==True and i<=lmts:
			for j in range(2*i,n,i):
				l[j]=False
		if l[i]==True:
			if(len(primes)>1):
				if(primes[-2]+i<2*primes[-1]):
					s+=1
					scount=scount[:primes[-1]]+([s]*(i-primes[-1]+1))
					strong.append(primes[-1])
			primes.append(i)
	#print(strong)
	return primes,scount
p,s=sieve()
t = int(input())
for i in range(t):
	l,r=map(int,input().split())
	print(s[r]-s[l-1])
