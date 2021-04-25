'''
https://hyperskill.org/learn/step/6465

Write a program that will help people who are going on vacation. 
The program should calculate the total required sum (e.g. $) of money to have a good rest for a given duration.

There are four parameters which have to be considered:

duration in days
total food cost per day
one-way flight cost
cost of one night in a hotel (the number of nights equal the duration of days minus one)
Read integer values of these parameters from the standard input and then print the result.

Hint

 Report a typo
Sample Input 1:

7
30
100
40
Sample Output 1:

650
 Write a program
'''
# put your python code here
t = [int(input()) for i in range(4)]
lst = [t[0] * t[1], t[2] * 2, t[3] * (t[0] - 1)]
print(sum(lst))
