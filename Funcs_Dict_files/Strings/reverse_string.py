def reverse(astring):
        """Write a function that reverses its string argument."""
        str=""
        for i in range(1,len(astring)+1):
                str= str+astring[-i]
        return str 
print (reverse("Hello World"))