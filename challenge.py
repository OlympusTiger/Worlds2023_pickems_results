from __future__ import annotations
from beginnercodes.challenges import test
from time import time
s=time()
def is_happy(n):
    sums=[]
    while n!=1 and n not in sums:
        sums.append(n)
        n=sum(map(lambda x:int(x)**2,str(n)))
    return n==1
test(790,is_happy)
print(time()-s)
s=time()
def is_happy(n):
    while n!=1:
        n=sum(map(lambda x:int(x)**2,str(n)))
        if '4' in str(n):
            return False
    return True
test(790,is_happy)
print(time()-s)






