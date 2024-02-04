from string import punctuation

with open("files/text.txt", "r") as text_file:
    text = text_file.readlines()

output_file = open("files/output_2.txt", "w")

for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(
        f"Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n")  # we take the whole sentence
    # except the last symbol because it is \n due to readlines function, and we don't want it

output_file.close()
