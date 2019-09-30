# Shallow copy eg1
orgList = [['1','2'],['3','4']]
copiedList =  orgList[:]
print(orgList,"\n",copiedList)
print(orgList is copiedList)
print(orgList==copiedList)
orgList[0].append('7')
print("orgList:", orgList, "\ncopiedList:",copiedList)
print ("-------------------")
orgList.append('8')
print("orgList:", orgList,"\ncopiedList:",copiedList)

## Shallow copy eg2
# original = [['dogs', 'puppies'], ['cats', "kittens"]]
# copied_version = original[:]
# print(copied_version)
# print(copied_version is original)
# print(copied_version == original)
# original[0].append(["canines"])
# print(original)
# print("-------- Now look at the copied version -----------")
# print(copied_version)

## Deep copy eg1
# import copy
# original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
# shallow_copy_version = original[:]
# deeply_copied_version = copy.deepcopy(original)
# original.append("Hi there")
# original[0].append(["marsupials"])
# print("-------- Original -----------")
# print(original)
# print("-------- deep copy -----------")
# print(deeply_copied_version)
# print("-------- shallow copy -----------")
# print(shallow_copy_version)