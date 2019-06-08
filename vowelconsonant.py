c=input()
l=['a','e','i','o','u','A','E','I','O','U']
if(c.isalpha()):
    if(c in l):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid ")
