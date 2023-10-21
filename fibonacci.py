a, b = 0, 1

while a < 10:

    print(a, b)

    a, b = b, a+b #The right-hand side expressions are evaluated from the left to the right.



'''
First iteration:
a = 0  b = 1

a = 1    b = 0+1 = 1

Second iteration:
a = 1  b = 1

a = 1, b = 1+1 = 2

Third iteration:
a = 1  b = 2

a = 2, b =  1+2 = 3

Fourth iteration:
a = 2  b = 3

a = 3, b = 2+3 = 5

Fifth iteration:
a = 3  b = 5

a = 5, b = 3+5 = 8

Sixth iteration:
a = 5 b = 8

a = 8, b = 5 + 8 = 13

Seventh  iteration:
a = 8, b = 13

a = 13, b = 8+13 = 21


'''