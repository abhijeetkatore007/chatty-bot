

lst = [int(input()) for i in range(3)]
indx = [70, 21, 15]
p  = list(map(lambda item, ind: item * ind, lst, indx))
print(sum(p) % 105)



# a20 = 10
# c = (int(a20) % 3) * 70
# print(c) 
# d = (int(a20) % 5) * 21 
# print(d)
# e = (int(a20) % 7) * 15
# print(e)
# b =((int(a20) % 3) * 70 + ((int(a20) % 5) * 21) + (( int(a20) % 7) * 15)) % 105
# print(b)