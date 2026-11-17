text = input("enter any text: ")

if any(char.isdigit() for char in text):
    print("Yes, there is number")             
else: 
    print("No, there is no number")