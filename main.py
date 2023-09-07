def replace_words():
    # Read file
    with open("file_to_read.txt", "r") as file:
        text = file.read()

    # Calculate total occurrences of "terrible"
    count = text.count("terrible")

    # Display total occurrences
    print(f"Total occurrences of 'terrible': {count}")

    # Replace even occurrences with "pathetic" and odd occurrences with "marvellous"
    words = text.split()
    new_words = []
    for i, word in enumerate(words):
        if word == "terrible":
            if (i+1) % 2 == 0:
                new_words.append("pathetic")
            else:
                new_words.append("marvellous")
        else:
            new_words.append(word)

    # Create new text with replaced words
    new_text = " ".join(new_words)

    # Write new text to result.txt
    with open("result.txt", "w") as file:
        file.write(new_text)

replace_words()
