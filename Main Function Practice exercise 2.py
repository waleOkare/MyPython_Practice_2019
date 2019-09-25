#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
def has_33(nums):
    
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            #nums[i:i+2] = [3,3] Alternative
            return True
        
    return False

print(has_33([1, 3, 3]))

#Given a string, return a string 
#where for every character in the original there are three characters.
def paper_doll(text):
    
    for letter in text:
       
        st = [letter * 3 for letter in text]
        
    return ( "".join(st))


#Alternative
#result = ''
#for char in text:
    #result += char * 3
#return result

print(paper_doll('Hello'))

#BlackJack: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
#return their sum. 
#If their sum exceeds 21 and there's an eleven, 
#reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):

        
    if sum ((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum ((a,b,c)) > 21 and 11 in (a,b,c): #checks the number 11 in a,b,c
        return sum((a,b,c)) - 10
    else:
        return "BUST"

print(blackjack(10,10,11))

#SUMMER OF '69: Return the sum of the numbers in the array, 
#except ignore sections of numbers starting with a 6 and extending to the next 9 
#(every 6 will be followed by at least one 9).
#Return 0 for no numbers.
def summer_69(arr):
        total = 0
        add = True
        
        for num in arr:
            while add:
                if num != 6:
                    total += num
                    break
                else:
                    add = False
            while not add:
                if num !=9:
                    break 
                else:
                    add = True
                    break
        return total

print(summer_69([2, 1, 6, 9, 11]))

#SPY GAME: Write a function that takes in a list of integers 
#and returns True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,0,2,4,0,5,7]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist 
#up to and including a given number
def count_primes(num):
    if num < 2:
        return 0
    
    primes = [2]
    x = 3
    
    while x <=num:
        
        for y in primes:
            if x%y == 0:
                x +=2
                break
        else:
                primes.append(x)
                x +=2
             
    print(primes)
    return len(primes)

print(count_primes(7))

#PRINT BIG: Write a function that takes in a single letter,
# and returns a 5x5 representation of that letter
def print_big(letter):
    
 
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4], 'F':[4,9,4,9,9]}
    
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

    

print_big('f')



