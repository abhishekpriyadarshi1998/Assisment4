#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

my_dict={}
for i in range(97,97+26):
    my_dict[chr(i)]=1
print(my_dict)    