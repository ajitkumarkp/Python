# #  map(<Trasformer i.e function or lambda expr>, <sequence>)
# #  Function takes in every item in the seq as input and returns the o/p
mList= [1, 2, 3, 4]
sqList= map (lambda val: val**2, mList)
print(list(sqList))

# #  filter(<Filter>, <sequence>)
# # <Filter> is a tranformer that only returns a BOOL
# #  Function takes in items in the seq and ONLY returns a binary True or False.
sList= ["apple", "mango", "berry"]
oList= filter (lambda value: "o" in value , sList)
print (list(oList))

# # Write a function called longlengths that returns the lengths 
# # of those strings that have at least 4 characters. Try it using map and filter.
def longlengths(strings):
    strings_4 = list (filter(lambda x: len(x)>4,strings))
    return list (map(len, strings_4))












