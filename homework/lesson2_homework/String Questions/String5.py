text = input("Enter any text: ")

vowels = sum(map(text.count, "aeiuo"))

only_letters = "".join(filter(str.isalpha, text))
all_letters = len(only_letters)

consonants = all_letters - vowels

print("Number of consenants is", consonants)
print("Number of vowels is", vowels)
