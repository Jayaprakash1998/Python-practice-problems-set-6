'''       QUESTION:

Humane Community :

Due to a virus outbreak, government has decided to implement a complete shutdown. 
All the people have been asked to stay and their homes to prevent the virus from spreading. 
For the first month people somehow managed with the supplies they had. 
But as the shutdown kept extending, people were not having enough supplies. 
Victor lived in a community, which had a row of houses. Each house had two lockers, 
one locker was kept out and one locker will be kept inside their house. 
Anyone from other community can choose an house at random, and they can either take two supplies from the locker or give two supplies if they wanted to, They are generous, 
but they cannot be over generous because that might lead them to loose all the supplies. So they have decided to limit the number of people entering the community everyday. 
At the end of the day, Victor wanted to calculate the number the gain or loss factor. 
He formulated a calculation procedure, which involves him multiplying the number of supplies left in the lockers left outside and the lockers inside the house for each house, 
then add these products of each house and that will give the factor value. 
That value was as least as possible. Help victor calculate the value.

Input Format : The first line of input has two spaced integer values N and K,
               where N is the number of houses in the community and K is the number of people who will be allowed to enter the community
               The Second line of input has the number of supplies kept in the outside locker
               The third line of input has the number of supplies kept in the lockers inside the house

Input Constraints : 
 1<=N, K<=10^3
-10^3<=a[i]<=10^3
-10^3<=b[i]<=10^3

Note: the number of supplies can be negative, as all the people in these community are generous, as if someone comes and asks for supplies, 
they will buy and give the supplies somehow, but for keeping track, they will store a negative value

Output Format : One single integer input specifying the gain or lock factor coined by Victor

Sample Input :
3 5
1 2 -3
-2 3 -5

Sample Output :
-31

















HINTS:

1 - Find the number which will yield a maximum magnitude.

2 - You have to take the supplies from one single house to get the minimum possible answer.

3 - Positive stands for subtracting whereas Negative stands for addition.

'''


































# ANSWER:

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
max_val = 0
max_in = 0
for i in range(n):
    if abs(b[i])>max_val:
        max_val = abs(b[i])
        max_in = i
a[max_in] = a[max_in] - 2 * k if(b[max_in]>0) else a[max_in] + 2 * k
s = 0
for i in range(n):
    s = s +  a[i] * b[i]
print(s)
