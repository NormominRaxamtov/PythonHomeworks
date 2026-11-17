text = input("enter any text: ")

bushliq = ""

seperate_text = text.split()

for word in seperate_text:
    bushliq = bushliq + word[0]

print(f'here is the qisqartirilgan versiyasi: {bushliq.upper()}')    


# text = input("enter anything: ")

# bushliq = "".join(word[0] for word in text.split()).upper()

# print(bushliq)