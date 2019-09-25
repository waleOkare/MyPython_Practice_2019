#use for, split function, if ' to create a statement that will print out words that start with 's'.
st = 'Print only the words that start with s in this sentence'.split()

for letter in st:
    if letter[0] == 's' or letter[0] == 'S':  
        print(letter)

#use range() to print all the even numbers from 0 to 10

for num in range(0, 11):
    if num % 2 == 0:
        print (num)

#use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [x for x in range(1,51) if x%3 == 0]
print(mylist)

#go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'.split()

for e in st:
    if len(e) % 2 == 0:
        print(e, 'is even!')

#A program that prints the integers from 1 to 100. but for multiples of three print "Fizz" instead of the number,
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

for num in range(1,101):
    
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

#Use List comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in the string'.split()

mylist = [letter[0] for letter in st]
print(mylist)

