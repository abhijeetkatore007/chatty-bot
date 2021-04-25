'''https://hyperskill.org/learn/step/6380

Find out if the result of dividing A by B is an odd number.

The input format:

The first line is the dividend (A) and the second line is the divisor (B). 
It is guaranteed that the numbers are divided without remainder.

The output format:

True or False






'''
i = [int(input()) for ii in range(2)]
lst = [i[0] / i[1]]
print(not sum(lst) % 2 == 0)
