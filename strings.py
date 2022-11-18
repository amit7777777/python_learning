# Python code to demonstrate working of
# len() and count()
str = "iPrimed software Training !"

# Printing length of string using len()
print (" The length of string is : ", len(str));

# Printing occurrence of "software" in string
# Prints 1 as it only checks till 50th element
print (" Number of appearance of ""software"" is : ",end="")
print (str.count("software",0,50))
