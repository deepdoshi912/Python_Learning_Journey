# Write a program to find out weather a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.
sub1 = int(input("Enter marks for subject 1:"))
sub2 = int(input("Enter marks for subject 2:"))
sub3 = int(input("Enter marks for subject 3:"))
sub4 = int(input("Enter marks for subject 4:"))

total_marks = sub1+sub2+sub3+sub4
percentage = (total_marks/400)*100

if (percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and sub4 >= 33):
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")
