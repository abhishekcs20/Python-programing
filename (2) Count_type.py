s = input()         # To input the string
vowels = 0
consonants = 0
digits = 0
space = 0
for i in range (0, len(s)):
    ch=s[i]         # To take the first letter of the string

    # To check whether the first element is vowel or consonant or digit or an space

    if( ( ch >= 'a' and ch <= 'z') or (ch >='A' and ch <= 'Z')):
        ch=ch.lower()

        if( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            vowels+=1
        else:
            consonants+=1

    if(ch >= '0' and ch <= '9'):
        digits+=1

    if(ch == ' '):
        space+=1
        
print('Number of Vowels are: ', vowels)
print('Number of Consonants are: ', consonants)
print('Number of Digits are: ', digits)
print('Number of Spaces are: ', space)
    
