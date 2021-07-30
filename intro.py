Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input(a)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    input(a)
NameError: name 'a' is not defined
>>> 
====================================================================================== RESTART: Shell ======================================================================================
>>> print("Welcome to PYTHON")
Welcome to PYTHON
>>> 
>>> 5+6
11
>>> 3*6+4
22
>>> print("sum= ",5+6)
sum=  11
>>> 5+6
11
>>> _+8
19
>>> name=input("Enter your name->")
Enter your name->
>>> 
>>> 
>>> 
>>> 
>>> name=input("Enter your name->")
Enter your name->Nain
>>> age=int(input("Enter your age->"))
Enter your age->18
>>> print("Hello",name)
Hello Nain
>>> print("Your age is",age)
Your age is 18
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
SyntaxError: invalid syntax
>>> "lets play together"
'lets play together'
>>> '"lets play together"'
'"lets play together"'
>>> 'lets play together"
SyntaxError: EOL while scanning string literal
>>> "how are you"'
SyntaxError: EOL while scanning string literal
>>> 'this' 'is' 'automatically' 'joined'
'thisisautomaticallyjoined'
>>> "India is beautiful country\
you must visit it"
'India is beautiful countryyou must visit it'
>>> "India is beautiful country\n
you must visit it"
SyntaxError: EOL while scanning string literal
>>> print(
KeyboardInterrupt
>>> print("India is beautiful country\n
you must visit it")
      
SyntaxError: EOL while scanning string literal
>>>  print("India is beautiful country\n\
you must visit it")
 
SyntaxError: unexpected indent
>>> print("india is a beautiful country\n \
you must visit it")
india is a beautiful country
 you must visit it
>>>  print("india is a beautiful country\n\
you must visit it")
 
SyntaxError: unexpected indent
>>> output="""
Program name-add two
Program author-Nain
Program description-Add two numbers
"""
>>> output
'\nProgram name-add two\nProgram author-Nain\nProgram description-Add two numbers\n'
>>> print(output)

Program name-add two
Program author-Nain
Program description-Add two numbers

>>> "Hello"+"World"
'HelloWorld'
>>> "Hello"+2+"all"
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    "Hello"+2+"all"
TypeError: can only concatenate str (not "int") to str
>>> "Hello"+str(2)+"All"
'Hello2All'
>>> "hello" "all"
'helloall'
>>> "Hello!"*5
'Hello!Hello!Hello!Hello!Hello!'
>>> "Hello"+"."*4+"nain"
'Hello....nain'
>>> print("-"*20)
--------------------
>>> \\
SyntaxError: unexpected character after line continuation character
>>> quarter=['jan','feb','march']
>>> type(quarter)
<class 'list'>
>>> print("directions=('East','West','North','South'))
      
SyntaxError: EOL while scanning string literal
>>>  print("directions=('East','West','North','South')")
 
SyntaxError: unexpected indent
>>> directions=('East','West','North','South')
>>> type(directions)
<class 'tuple'>
>>> code={'asr':'0183','jld':'0181'}
>>> type(code)
<class 'dict'>
>>> my_set={1,2,3}
>>> type(my_set)
<class 'set'>
>>> import sys
>>> print(sys.maxsize)
2147483647
>>> flag 4>2
SyntaxError: invalid syntax
>>> flag=4>2
>>> print(flag)
True
>>> 