'''       QUESTION:

Commander of The Force :

You are the Commander of the force. You have soldiers with numbers written on their shields. A soldier would not accept to fight with another soldier's shield. 
Shield numbers are a series. That is sums of distinct powers of 4.

Your assistant will tell you the shield number, you have to give the shield to the right soldier. Soldiers are also numbered from 1. 
They are standing in the ascending order.

You time-traveled to 2020 and learned to program. Now go back to your time and write a program to give the right shield to the right soldier.

You are given with a shield number N, find the soldier number who you have to return the shield. 
Sometimes the shield number might have tampered, so if the number will not be able to be given to anyone, you have to return back with the shield.

Input Format : Single integer N

Input Constraints : 1<=N<=10^9

Output Format : Single integer or "RETURN" if you have to return with the shield

Sample Input :
18

Sample Output :
RETURN















HINTS:

1 - Binary.

2 - Solution is O(1).Find the Sequence.

3 - It is Moser–de Bruijn sequence.

'''

















































# ANSWER:

n = int(input())
k = bin(n)[2:]
if(int(k[1::2])==0 and len(k)%2!=0):
    print(int(k[::2],2))
else:
    print("RETURN")
