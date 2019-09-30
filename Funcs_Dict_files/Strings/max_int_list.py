import random

def max_no(mlist):
        """Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value."""
        print(max(mlist))      
        max_int=0
        for val in mlist:
                if val>max_int:
                        max_int=val           
        return max_int    
       
my_list=[]
for i in range(100):
        my_list.append(random.randrange(0,1000))

print(max_no(my_list))
