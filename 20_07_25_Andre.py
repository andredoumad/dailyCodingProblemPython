'''
Andre Doumad

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#  car(cons(3, 4)) returns 3
def car(x):
    print(x)
    print('car a: ' + str(x.__closure__[0].cell_contents))
    def first(a,b):
        print('first a: ' + str(a))
        print('first b: ' + str(b))
        return a
    return x(first)
print('result of car(cons(3, 4)): ' + str(car(cons(3, 4))))

# cdr(cons(3, 4)) returns 4
def cdr(x):
    print(x)
    print('car b: ' + str(x.__closure__[1].cell_contents))
    def last(a,b):
        print('last a: ' + str(a))
        print('last b: ' + str(b))
        return b
    return x(last)
print('result of cdr(cons(3, 4)): ' + str(cdr(cons(3, 4))))
