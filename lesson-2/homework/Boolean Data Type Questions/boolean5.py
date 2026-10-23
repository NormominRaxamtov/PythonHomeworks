text1 = input("enter the first text: ")
text2 = input("enter the second text: ")

len_text1 = len(text1.strip())
len_text2 = len(text2.strip())

if len_text1 == len_text2:
    print("they have the same length.")
else:
    print("they have not the same length")    