def reverse(astring):
        """Write a function that mirrors its string argument, generating a string containing the original string and the string backwards."""
        str=""
        for i in range(1,len(astring)+1):
                str= str+astring[-i]
        return (astring,str)
print (reverse("Hello World"))