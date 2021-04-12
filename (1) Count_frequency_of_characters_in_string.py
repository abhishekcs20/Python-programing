# Program which return the frequency of characters
def get_freq(lower_word):
    return {x:lower_word.count(x) for x in 'abcdefghijklmnopqrstuvwxyz'}    #Dictionary comprehension method


# Runner code
word = input()
lower_word = word.lower()   #string method
output = get_freq(lower_word)   #calling function
print(output)
