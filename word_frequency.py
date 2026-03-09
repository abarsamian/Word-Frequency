import re



filename = input ("Please enter file name: ")

word_counts = { }

ig_lst = ["a", "an", "and", "i", "the", "so", "to", "in", "are", "is", "at", "on"]


with open(filename, "r") as file:
    for line in file:
        line = line.lower()
        #this is where we make the line read without punctuation
        line = re.sub(r"[^a-z\s]","", line)
        words = line.split()

        for word in words:
            if word in ig_lst:
                continue
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    print("Total unique words", len(word_counts))

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    print("Here are the top 10 Most frequent words: ")

    for word, count in sorted_words[:10]:
        print(word, ":", "*" * count, "(",count,")" )

