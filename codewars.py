#https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
# We need a function that can transform a number (integer) into a string.
# 
# What ways of achieving this do you know?
# 
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100
def number_to_string(num):
    return str(num)

#https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
#Write a function that removes the spaces from the string, then return the resultant string.

# Examples (Input -> Output):

# "8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
# "8aaaaa dddd r     " -> "8aaaaaddddr"

def no_space(x):
    return x.replace(" ", "")
    

# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.
def get_count(sentence):
    count = 0
    vowels = "a,e,i,o,u"
    for i in sentence:
        if i in vowels:
            count +=1
    return count