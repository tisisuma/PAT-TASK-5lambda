from functools import reduce

#using reduce function to iterate the sequence and calculate it till 50

fib_numbers = lambda y: reduce(lambda x, _: x + [x[-1] + x[-2]], range(y - 2), [0, 1])




print(fib_numbers(50))