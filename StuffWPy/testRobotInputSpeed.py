import time
import keyboard
import random
import timeit


a1 = "acbdefghijklmnopqrstuvwxyz0123456789`1234567890-=~!@#$%^&*()_+[]\{}|;':\",./<>?"
a2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
alpha = a2
line=''
chars  = 200-8

for i in range(chars):
    line += alpha[random.randint(0, len(alpha)-1)]

line = 'echo "' + line + '"\n'
print(len(line))
keyboard.wait('esc')


def my_function():
    keyboard.write(line)

print(timeit.timeit(my_function, number=20)/20)
keyboard.wait('esc')
