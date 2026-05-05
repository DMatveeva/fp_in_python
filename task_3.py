from pymonad.list import ListMonad
from pymonad.maybe import Just
from pymonad.tools import curry


@curry(2)
def add(x, y):
    return x + y
  
def add10(x):
    return x.then(add(10))
  
a = add10(Just(5))
print(a)

l = ListMonad(1,2,3)
b = add10(l)
print(b)
