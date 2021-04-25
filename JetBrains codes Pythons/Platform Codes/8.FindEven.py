'''
https://hyperskill.org/learn/step/6542#solutions
Write a program that prints all positive even numbers less than the input number. Please, use the while loop for that.

The input format:

The maximum number N varying from 1 to 200.

The output format:

All positive even numbers that are less than N. Print them in the ascending order. Each number must be on a separate line.

 Report a typo
Sample Input 1:

8
Sample Output 1:

2
4
6


'''




n = int(input())
lst = []
while n > 0:
    n -= 1
    if n % 2 == 0 and n != 0:
        lst.append(n)
    
i = 0
while i < len(lst):
    i += 1
    print(lst[-i])

'''

maximum = int(input())
counter = 2

while counter < maximum:
    if not counter % 2:
        print(counter)
    counter += 1
 
 '''

 '''
n = int(input())
a = 1
while a < n:
    if a % 2 == 0:
        print(a)
    a += 1


 '''



 '''
limit = int(input())
n = 2
while n < limit:
    print(n)
    n += 2

 '''


'''
N = int(input())
k = 0
while k < N - 2 and 1 < N <= 200:
    k += 2
    print(k)


'''

'''
num = int(input())
i = 0
while i < num - 2:
    i += 2
    if i % 2 == 0:
        print(i)

'''