#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T = int(input())
for test_cases in range(1,T+1):
    days = int(input())
    breaking_days = 0
    
    visitor = list(map(int, input().split()))
    #visitor = [input().split(' ') for i in range(days)]
    if(days==1):
        breaking_days = 1
    if(days>1):
        if(visitor[0] > visitor[1]):
            breaking_days += 1
        
    max_visitor = visitor[0];
    for index in range(1,len(visitor)):
        if(visitor[index] > max_visitor):
            if(index == len(visitor)-1):
                breaking_days += 1
            else:
                if(visitor[index] > visitor[index+1]):
                    breaking_days += 1
            max_visitor = visitor[index]
    print("Case #{}: {}".format(test_cases, breaking_days))


# In[ ]:




