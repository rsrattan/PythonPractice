word = input("Input a String: ")
print(f"Orginal String is  {word}\nPrinting only even index chars")
for i in range(0, len(word), 2):
    print(word[i])