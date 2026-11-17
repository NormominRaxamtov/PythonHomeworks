text = input("enter any text: ")

all_vowels = "aeiuoAEIUO"

for vowels in all_vowels:

    text = text.replace(vowels, "*")

print(text)
