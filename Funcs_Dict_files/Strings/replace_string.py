def replace(s, old, new):
        """Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:"""
        return (new.join(s.split(old)))
        
s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace(s, "om", "am"))
