'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, 
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

We will be sending the solution tomorrow, along with tomorrow's question. 
'''
# def staircase(n, X):
#     print(n)
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     elif n in X:
#         return 1 + sum(staircase(n - g, X) for g in X if g < n)
#     else:
#         return sum(staircase(n - g, X) for g in X if g < n)

def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]



print('unique ways: ', staircase(4, [1,2]))
print('unique ways: ', staircase(4, [1,3,5]))
print('unique ways: ', staircase(4, [1,2,3]))