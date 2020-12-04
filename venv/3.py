# _*_ coding: utf-8 _*_
a=['a','b',"c"]
print (len(a))
age = 20
if age >=18:
    print("your age is", age)
    print ('adult')
age = 136
if age >= 18:
    print ('yong man')
elif age>= 6:
    print ('big boy')
else:
    print ('婴儿')

i = '89'
type = ['1','2','8']
if i in type:
    print (i)
else:
    print ('sorry')
x ={'1'}

if x:
    print ('True')
else:
    print ('false')

s = input ("birth:")
birth = int(s)
if birth <2000:
    print ('00前')
else:
    print ("00后")


s= input('wuliao')
wuliao =int(s)
if wuliao < 2000:
    print ('00后')
elif wuliao >20:
    print ('90后')
else:
    print ('渣渣')