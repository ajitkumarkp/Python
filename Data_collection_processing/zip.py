# Adding elements of 2 lists 
L1= [1,2,3,4]
L2= [11,12,13,14]

# zip packs the elements of the 2 lists into a tuple
L3 = list (zip (L1,L2))
print(L3)
L4=[]
for x,y in L3:
    L4.append(x+y)
print(L4)

# using List comprehension and zip
L4 = [x+y for x, y in list(zip(L1,L2))]
print(L4)


# Another example
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x+y for (x,y) in zip(L1,L2) if x>10 and y<5]
print(L3)


## Write code using zip and filter so that these lists (l1 and l2)
## are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = list(zip(l1,l2))
opposites = list(filter(lambda tup: len(tup[0])>3 and len(tup[1])>3, l3)) 
print (opposites)


## Below, we have provided a species list and a population list. 
## Use zip to combine these lists into one list of tuples called
## pop_info. From this list, create a new list called endangered 
## that contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species, population))

endangered = [tup[0] for tup in pop_info if tup[1]<2500]
#or 
endangered_1 = [sp for (sp,pop) in pop_info if pop<2500]

print (endangered,endangered_1)