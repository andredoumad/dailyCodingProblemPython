# Andre Doumad
'''
This problem was asked by Google.

The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
import random


def solution():
    circlePoints=squarePoints=0
    iterations = 1000

    while iterations > 0:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        originDistance = x**2 + y**2
        if originDistance<=1:
            circlePoints+=1
        squarePoints+=1
        iterations-=1
    pi = 4*(circlePoints/squarePoints)
    return pi

print(solution())
print(solution())
print(solution())
print(solution())
print(solution())
print(solution())
print(solution())

'''
OUTPUT:
3.144
3.12
3.14
3.2
3.128
3.008
3.208
'''