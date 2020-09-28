#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random
from functools import wraps
from autoBankForpupil import createOperators,createProperFractionPro
  
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running : \n%s seconds" %(str(t1-t0)))#function.func_name,
    return result
  return function_timer

@fn_timer
def myfunction(n):
    return sorted(createProperFractionPro(2,2))

if __name__ == "__main__":
  myfunction(100000)


# In[ ]:




