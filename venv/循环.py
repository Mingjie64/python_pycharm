# _*_ coding: utf-8 _*_

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum =0
for i in l:
    sum = sum + i
print (sum)


a =list(range(5))

print (a)

sum = 0
for i in range(101):
    sum =sum +i
print (sum)

sum = 0
n=99
while n>0:
    sum = sum + n
    n = n - 2
print (sum)


n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print ('END')



n = 0
while n <10:
    n = n +1
    if n % 2 == 0:
        continue
    print (n)

n =1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n +1
print ('END')

n  = 0
while n <10:
    n = n + 1
    if n % 2 == 0:
        continue
    print (n)

d = {'michale':95,'bob':75,'tracy':85}
print (d['bob'])
print (d.get('body',-1))
d.pop('bob')
print (d)

s= set([1,2,3,])
print (s)
s.add(4)
print (s)
s.remove(4)
print (s)
n = 0
while n <10:
    n = n + 1
    if n % 2==0:
        continue

    print (n)