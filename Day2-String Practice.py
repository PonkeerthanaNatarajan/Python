Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hour challemge")
30 days 30 hour challemge
>>> print('30 days 30 hour challenge")                                           Hours = "thirty"
print(Hours)
      
SyntaxError: EOL while scanning string literal
>>> Hours="thirty"
>>> print(Hours)
thirty
>>> Days="Thirty days"
>>> print(Days[5])
y
>>> Challenge="I will win"
>>> print(Challenge[7:10])
win
>>> Challenge="I will win"
>>> print(len(Challenge))
10
>>> Challenge="I will win"
>>> print(Challenge.lower())
i will win
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+" "+b
>>> print(c)
30 Days 30 hours
>>> text="Thirty days and Thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> text="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> x=text.capitalize()
>>> print(x)
Don't trouble trouble until trouble troubles you
>>> text="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find("UNTIL")
>>> print(x)
22
>>> x=text.find("UNTIL",10,30)
>>> print(x)
22
>>> text="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> x=text.isalpha()
>>> print(x)
False
>>> text="DON'T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> x=text.isalnum()
>>> print(x)
False
>>> 