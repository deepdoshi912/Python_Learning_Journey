# Write a program to find out weater a given post is talking about "Deep" or not.

post = input ("Enter the post: ")

if("Deep".lower() in post.lower()):  #.lower() is used to convert the string to lowercase, so that the program can find "Deep" in the post regardless of the case (e.g. "deep", "DEEP", "DeEp", etc.).
    print("The post is talking about 'Deep'.")
else:
    print("The post is not talking about 'Deep'.")