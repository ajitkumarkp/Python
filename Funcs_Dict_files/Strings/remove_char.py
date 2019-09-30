def remove_letter(theLetter, theString):
        """Write a function that removes all occurrences of a given letter from a string."""
        thelist= theString.split(theLetter)
        str=""
        for char in thelist:
                str=str+char
        return(str)

print (remove_letter("l", "helloworld"))