Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# default values of individual datatypes

"""
integer - 0/ int()
float - 0.0/float()
complex - 0j/0+0j/complex()
boolean - False
"""

# strings

s = 'hello world "welcome!!!!" '
s1 = "hello world"
s2 = '''helloo world'''
s3 = """hello world"""

# default values

#s = '', "", '''''', """"""
s1 = str()


# length 
len(s)

name = input("enter the name:")
string = f"My name is {name}"

s = "My name is %s"%name

