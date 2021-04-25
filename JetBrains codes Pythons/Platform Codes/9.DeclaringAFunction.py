'''
https://hyperskill.org/learn/step/5907#hint
Declaring a function 
Make the function work
The function closest_higher_mod_5 takes exactly one integer argument x and returns the smallest integer y such that:

y is greater than or equal to x,
y is divisible by 5.
Correct the last line of the code below to make the function work.

Hint

Try to think about how the variable remainder might be useful to you.
 Report a typo
HINT by 
avatar
 apollinaria
Thought process to help:

1. Look at the pattern for modulo operators: 40 % 5 = 0, 41 % 5 = 1, 42 % 5 = 2, 43 % 5 = 3, etc. 0,1,2,3 are the remainders after the modulo.
2. What's the relationship (distance) between the remainder and the next divisible integer? ex. for 41, remainder 1, we are (5-1) away from 45, so (5 - remainder) and since we know the remainder is (x % 5), we can say we are (5 - (x % 5)) away from the next divisible integer.
3. Add that distance to x t find the next divisible integer.
Was this hint helpful?
Sample Input 1:

40
Sample Output 1:

40
Sample Input 2:

43
Sample Output 2:

45


'''
def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return x + (5 - remainder)
