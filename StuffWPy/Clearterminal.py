import os
print("something to test")
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
clear()
input()
