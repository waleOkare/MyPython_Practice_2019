#Write a function that computes the volume of a sphere given its radius.
#The volume of a sphere is given as: 4/3 pi r^3

def vol(rad):
    
    volume = 4/3 * 3.14 * rad**3    
    return volume

print(vol(2))

#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):

        if low == high:
            print('Your error! Low and High digits are the same!')

        elif num >= low and num <= high:

            return num, 'is in the range between', low, 'and', high

        else:
            return False

print(ran_check(5,2,7))

#Write a function that checks whether a number is in a given range. (True or False)
def ran_bool(num, low, high):

        if num in range(low,high):
            return True
        else:
            return False

print(ran_bool(5,1,15))


#Write a Python function that accepts a string and
#calculates the number of upper case letters and lower case letters.

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)




#Write a Python function that takes a list and
#returns a new list with unique elements of the first list.

def unique_list(lst):

    return set(lst)
#Alternative
    #x = []
   # for a in lst:
        #if a not in x:
           # x.append(a)
    #return x


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


#Write a Python function to multiply all the numbers in a list.

import numpy

def multiply(numbers):
    return numpy.prod(numbers)


#Alternative

    #prod = numbers[0]
    #print(numbers)
    #for x in numbers:
        #prod *= x
        #pass

    #return prod

print(multiply([1,2,3,-4]))

#Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(s):

    if s == s[::-1]:

        return True
    else:
        return False

print(palindrome('hannah'))


#Write a Python function to check whether a string is pangram or not.
import string
def ispangram(str,alphabet=string.ascii_lowercase):
    word = str
    for i in word:
        if i in string.ascii_lowercase:
            return True
        else:
            return False

print(ispangram("The quick brown fox jumps over the lazy dog"))

print(string.ascii_lowercase)


