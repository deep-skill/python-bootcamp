import math
from functools import reduce
from math import factorial as fact

from mates import mates
import mates.mates
from mates.mates import factorial
from mates.mates import gcd
from mates.mates import to_square


print(fact(4))
print(math.factorial(5))
print(reduce(lambda n1, n2: n1 + n2, [1, 2, 3, 4, 5]))

print(factorial(5))
print(gcd(8, 19))
print(to_square(10))

print(mates.mates.gcd(8, 18))
#print(mates.to_square(12))
