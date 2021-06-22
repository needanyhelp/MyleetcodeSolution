
from collections import OrderedDict
from typing import List
import collections

def kFrequency(s:List[int], k:int)->List[int]:
    nums=collections.Counter(s)
    ordered_d1 = OrderedDict(sorted(nums.items(), key=lambda t:t[1], reverse=True))

    print(list(ordered_d1)[:2])

kFrequency([1,1,1,2,2,3], 2)



