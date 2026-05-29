# A spam comment id=s defined as a text containing following keywords:
# Make a lot of money", "Buy now", "Click this", "Subscribe this".
# Write a program to detect these spams.

p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Click this"
p4 = "Subscribe this"

massage = input("enter the massage: ")
# if (massage == p1 or massage == p2 or massage ==p3 or massage == p4):
    # print("This is a spam comment.")

# This statement is also correct 
if ((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This is a spam comment.")
else:
    print("This is not a spam massage.")