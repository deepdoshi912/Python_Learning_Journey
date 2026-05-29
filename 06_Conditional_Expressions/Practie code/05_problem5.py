#Write a program which finds out weather a given name is a present in a list or not.
names = ["Deep", "Yash", "Sandeep", "Anubhav", "Meet"]

name = input("Eneter the name: ")

if name in names:
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")