

#Average

def average_of_three(num1,num2,num3):
    return (num1 + num2 + num3 )/float(3)
    
print (average_of_three(5,2,3))

#Goodbye


def say_goodbye(name):
    return 'Goodbye {}'.format(name)

print(say_goodbye('Jabulile'))

#Palidrome

def is_palindrome(word):
    upperWord= word.upper()
    i =len(word)-1
    reverse_word =""
    while(i>=0):
        reverse_word = reverse_word+upperWord[i]
        i= i=i-1
    if(reverse_word==upperWord):
        return True
    else:
        return False
word = raw_input("Enter a word: ")
print(is_palindrome(word))

#Doubler

def doubler(numbers):
    i=0;
    for num in numbers:
        numbers[i]= num*2
        i=i+1
    return numbers
    
print(doubler([1,2,3,4]))

#Fizzz Buzz

def fizz_buzz(max):
    arr =[]
    for n in range(max):
        if(n%4 == 0 and n%6!=0):
            arr.append(n)
        elif(n%4!=0 and n%6==0):
            arr.append(n)
        else:
            continue
    return arr
    
print(fizz_buzz(30))

