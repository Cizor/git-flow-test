import os

a = input("Choose one of following:\n1. Tell os name\n2. Tell current working directory\n3. Goodbye\nTell your option: ")
if int(a) == 1:
    print(os.uname())
elif int(a) == 2:
    print(os.getcwd())
elif int(a) == 3:
    print("Goodbye")
    exit(0)
else:
    print('Invalid option')
    exit(0)
