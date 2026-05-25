# Write a program to fill in a letter tempplate to given below with name and date.
letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''
 
print(letter.replace("<|Name|>","Deep Doshi").replace("<|Date|>","20 May 2060"))
