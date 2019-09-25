
#A function that returns the lesser of two given numbers 
#if both numbers are even, but returns 
#the greater if one or both numbers are odd.
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    
    elif a % 2 != 0 or b % 2 != 0:
            return max(a,b)

print(lesser_of_two_evens(13,33))


#Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    word = text.split()
    
    if word[0][0].lower() == word[1][0].lower(): #lower(), convert all characters to lowercase
        return True
    else:
        return False
    

print(animal_crackers('Barry Barry'))


#Given two integers, return True if the sum of the integers is 20 or 
#if one of the integers is 20. If not, return False.

def makes_twenty(num1,num2):
    if sum((num1,num2)) == 20 or num1 == 20 or num2 == 20:
        return True
    else:
        return False
        
#return (num1 + num2) ==20 or num1 == 20 or num2 == 20

print(makes_twenty(50,20))

#Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    
    st = name[1:3]
    st1 =  name[4:]
    
    return name[0].capitalize() + st + name[3].capitalize()  + st1
    
   
#Alternative
#first_half = name[:3]
#second_half = name[3:]
#return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))

#Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    #Alternative
    #word = text.split()
    #st = reversed(word)
    #for word2 in st:
       #print (word2, end =' ')
         
    word = text.split()
    st = (word[::-1]) #reverse the text
    
    return ( " ".join(st))#.join function used to join a list

print(master_yoda('Babawale Patrick Okare '))

#Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
   # num = abs(n) #abs(n) returns the absolute value of a number
    num = n
    if (abs(num >= 90)) and (abs(num <= 110)) or (abs(num>=190)) and (abs(num<=210)):
        return True
    else:
        return False
 #Alternative
   # return (abs(100-n) <=10) or (abs(200-n) <=10)

print(almost_there(100))


mylist = ['a', 'b','c','d']
print('-----'.join(mylist))





