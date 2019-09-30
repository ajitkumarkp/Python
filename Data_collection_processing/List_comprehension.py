#  [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]
mList = [1,2,3,4,5,6,7,8,9,10]
nList = [i for i in mList if i%2]
print(nList)

#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
things = [3, 4, 6, 7, 0, 1]
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))
# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])

# assign to the variable compri all the values of the
# key name in any of the sub-dictionaries in the dictionary tester.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
import json
print (json.dumps(tester, indent=2))
compri = [dict["name"] for dict in tester["info"] if True]
print (compri)

# # Challenge: Below, we have provided a list of lists that contain numbers. 
# # Using list comprehension, create a new list threes that contains all the numbers from the original list that are divisible by 3. This can be accomplished in one line of code.
nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]
threes = [num for L in nums for num in L if num%3==0]
print (threes)

# Using accumulation method
threes = []
nums = [[4, 3, 12, 10], [8, 7, 6], [5, 18, 15, 7, 11], [9, 4], [24, 20, 17], [3, 5]]
for L in nums:
   for num in L:
       if num%3==0:
           threes.append(num)
print (threes)

