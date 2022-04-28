Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
names=["Harry Potter","Dumbledoere","Voldemort"]
names.extend(["Ron"])
print(names.extend(["Ron"]))
None
print(names)
['Harry Potter', 'Dumbledoere', 'Voldemort', 'Ron', 'Ron']
names=["Harry Potter","Dumbledoere","Voldemort"]
names=["Harry Potter","Dumbledoere","Voldemort"]names.extend(["Ron"])
SyntaxError: invalid syntax
print(namesnames=["Harry Potter","Dumbledoere","Voldemort"]names.extend(["Ron"])
      
SyntaxError: '(' was never closed
names.extend(["Ron"])
      
print(names)
      
['Harry Potter', 'Dumbledoere', 'Voldemort', 'Ron']
a=["mary","had","a","little","lamb"]
      
print(l)
      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(l)
NameError: name 'l' is not defined
print(l.sort())
      
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(l.sort())
NameError: name 'l' is not defined
print(a.sort())
      
None
a=["mary","had","a","little","lamb"]
      
print(a.sort())
      
None
data=["python",[82,2+3j,["ruby","perl",100]],"java"]
      
data[1][1][2]
      
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data[1][1][2]
TypeError: 'complex' object is not subscriptable
"12:45".isdigit()
      
False
s="%%%&^@#hai*&^^&&%"
      
s.strip("%&^@#*)
        
SyntaxError: unterminated string literal (detected at line 1)
s.strip("%&^@#hello)
        
SyntaxError: unterminated string literal (detected at line 1)
s="hello world"
        
print(s[-9:2:-1)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(s[-9:2:-1])
      

