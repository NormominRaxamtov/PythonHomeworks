text = input("enter any text: ")

total = "".join(filter(str.isalpha, text))
number_of_words = len(total)
print(f"here is the number of that text: {number_of_words}")