# 1.Basic - print all the integers from 0 to 150
num = 0
while num <= 150:
    print(num)
    num += 1

# 2.Multiple of Five - print all the multiples of 5 from 5 to 1000
for num in range(5,1001,5):
    print(num)

""" 3. Counting, the Dojo Way -  print integrs from 1 to 100. if divisible by 5, 
print "coding" instead. if divisiblle by 10, print "Coding dojo"""
for num in range(1,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and  print the file sum.
SumOddInteger = 0
for num in range(1, 500001, 2):
    SumOddInteger += num
    print("Sum of odd integers from 0 to 500,000", SumOddInteger)

# 5. Countdown by fours - Print positive numbers starting at 2018, counting down by 4
for num in range(2018,0,-4):
    print(num)

""" 6. flexible Counter- Set three variables: lowNum, highNum, mult. Starting at
lowNum and going through highNum, print only the integers that are a multiple of mult.
for example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9(on successive lines)
"""
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)