import os

x = input("Enter yout main Folder")
a = input("Enter yout sub Folder number 1")
b = input("Enter yout sub Folder number 2")

if not os.path.exists(x):
    os.mkdir(x)
    if not os.path.exists(a):
        os.chdir(x)
        os.mkdir(a)
    if not os.path.exists(b):
        os.mkdir(b)
