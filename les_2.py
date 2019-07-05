#строки
s = input("введите предложение ")
print(s[2])

s = input("введите предложение ")
print(s[-2])

s = input("введите предложение ")
print(s[0:5])

s = input("введите предложение ")
print(s[0:-2])

s = input("введите предложение ")
print(s[::2])

s = input("введите предложение ")
print(s[1::2])

s = input("введите предложение ")
print(s[::-1])

s = input("введите предложение")
a = format(s[1::2])
print(a[::-1])

s = input("введите предложение ")
print(len(s))

#числа

a = [36, 67, 76, 5, 10, 98, 10,]
print(min(a))
print(max(a))

a = []
a.append((0,1)*6)
print(a)

b = [0, 0, 0, 0, 0]
b.append(1)
b.insert(0, 1)
print(b)

c = [95, 67, 98, 5, 43, 5, 7, 6, 12, 87, 12, 5, 87, 12]
c.sort()
for i in c:
    if c.count(i) >= 2:
        print(i)

# года полиндром

a = []
for b in range(11,2020):
    b = str(b)
    if b == b[::-1]:
        if b not in a:
            a.append(b)
print (a)