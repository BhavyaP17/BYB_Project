# Roman to Integer in Python
"""
Numeral	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

suppose the numeral is 'II', so this is 2, there are two 'I's are added together. For XII, it is 12, so this is actually X + II = 10 + 2 = 12. The roman numerals of 4 are not IIII, it is IV. This is a little tricky.

I can be used before V(5) and X(10) to make it 4 and 9 respectively

X cab be used before L(50) and C(100) to make it 40 and 90 respectively

C can be used before D(500) and M(1000) to make them 400 and 900 respectively.

In this case, we will create one Roman to integer converter, that can convert numbers from 1 to 3999.

To solve this, we will create some possible numerals and their values and some special values like 4, 9, 40, 90, 400, 900. Now scan the given string, if some substring is present in the table, then take its value into result, then check for the next, for next match, it adds the value with the result, finally forms the number.

Running the program:
Download the files in the repo on your machine, open the python file with your preferred IDE.

"""
