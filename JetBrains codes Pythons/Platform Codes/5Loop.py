'''
In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay. 
More precisely, it is the time required for an element to reduce in half.

Let's take an isotope of Radium (Ra) called radium-223. Its half-life is about 12 days: this means that every 12 days the number of atoms reduces in half.

Your program should:

read the initial and the final quantity of atoms from the input.
count how many complete half-life periods it would take for the initial number of atoms of radium-223 to become equal to or go below the final quantity. 
Note that the number of half-life periods should be an integer, not a float!
multiply the number of half-life periods by 12 to convert the number of half-life periods to days.
output the resulting number of days that it takes for the initial number of atoms to go below the final number.
For example, the initial number of atoms is 4 and the resulting quantity is 3. After the first half-life period, 
the initial number will reduce to 2 atoms, which is below 3. Then, we take the number of half-life periods that have passed (1) and 
multiply it by the number of days that every half-life period takes (12). The output will be 12.

The input format:

The first line: the initial quantity of atoms (from 2 to 1,000,000).

The second line: the final quantity of atoms.

The output format:

The number of days that it would take for radium-223 to go from the initial quantity of atoms to or below the final quantity of atoms.

An example:

The initial quantity is 8, the final quantity is 3. Your program output should be number 24.

 Report a typo

 Sample Input 1:

4
3
Sample Output 1:

12
Sample Input 2:

835950
139505
Sample Output 2:

36


'''

lst = [int(input()) for i in range(2)]
count = 0
b = lst[1]  # remaining
c = True
while c:
    count += 1
    
    lst[0] = lst[0] // 2
    if lst[0] <= b:
        c = False
        count = count * 12
        print(count)


'''
Initial is 20, final is 3.
First try: 20//2 # This gives you 10 which is greater than 3. So go again
Second try: 10//2 # gives you 5 which is greater than 3. Go again
Third try: 5 // 2 # gives you 2 which is less than 3

So you ran 3 tries. The answer is: 3 * 12 = 36
avatar
aghogho monorien
about 1 month ago
Moderator
Explaining the first example:
Initial 4, final 3.
First try: 4 // 2 gives 2 which is less than 3

Answer = 12 * 1 = 12

Example 2:
Initial: 835950, final: 139505

1: 835950 // 2 = 417975
2: 417975 // 2 =208987
3: 208987 // 2 = 104493

It took 3 tries to get to less than or equal to the final AMT. Ans = 3 * 12 = 36.

Kindly turn this into code.

'''

import math

print(12 * math.ceil(math.log2(int(input()) / int(input()))))


''''''

quantity, final = int(input()), int(input())
periods = 0

while quantity > final:
    quantity /= 2
    periods += 1

print(periods * 12) 
