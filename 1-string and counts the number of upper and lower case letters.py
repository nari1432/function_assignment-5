##.Write a Python function that accepts a string and counts the number of upper and lower case letters.
#ample String : 'The quick Brow Fox'
#xpected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12


def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (u,l))

up_low('The quick Brow Fox')