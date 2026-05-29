# Write a program to find weather a given username contains less than 10 cahrecters or not.
un = input("Enter the username: ")

if(len(un)<10):
    print("Your username contains less than 10 characters.")
else:
    print("Your username contains 10 or more characters.")
