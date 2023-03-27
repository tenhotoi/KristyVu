def testing():
    print('Hello World')

testing()

d = {1: 10, 2: 20, 3: 30}
print(list(d))

lst = [1,2,3,4,5]
print('\n',lst[-1::-1])
print(lst[-1::-2])
print(lst[-1::-3])

print('\n',lst[-1:0:-1])
print(lst[-1:0:-2])
print(lst[-1:0:-3])

print('\n',lst[-1:1:-1])
print(lst[-1:1:-2])
print(lst[-1:1:-3])

print('\n',lst[1:-1:-1])
print(lst[2:0:-1])
print(lst[3:0:-1])

print('\n',lst[1:2:-1])
print(lst[1:2:-2])
print(lst[1:2:-3])

print('\n',lst[0:1])
print(lst[0:2])
print(lst[0:3])

print('\n',lst[-1:3:-1])
print(lst[1:0:-1])
print(lst[:0:-1])

a = input()
print(a[:-1])