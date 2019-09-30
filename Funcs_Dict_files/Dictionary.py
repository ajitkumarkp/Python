### Create the dictionary characters that shows each character from the string sally and its frequency. 
### Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters ={}

sally_list=sally.split()

for str in sally_list:
    if str not in characters:
        characters[str]=0
    characters[str]=characters[str]+1

print("characters:",characters)

char_list = list(characters.keys())
print("char_list:",char_list)

max=characters[char_list[0]]
print("max:", max)

for key in char_list:
    if characters[key]>=max:
        max=characters[key]
        best_char= key  

print(best_char)


### Do the same as above but now find the least frequent letter.
### Create the dictionary characters that shows each character from string sally and its frequency. 
### Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"
characters ={}
for char in sally:
    if char not in characters:
        characters[char]=0
    characters[char]=characters[char]+1

print("characters:",characters)

char_list = list(characters.keys())
print("char_list:",char_list)

min=characters[char_list[0]]
print("min:", min)

for key in char_list:
    if characters[key]<=min:
        min=characters[key]
        worst_char= key  

print(worst_char)


###Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. 
###Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for char in string1:
    if char.lower() not in letter_counts:
        letter_counts[char.lower()]=0
    letter_counts[char.lower()]=letter_counts[char.lower()]+1
print(letter_counts)























