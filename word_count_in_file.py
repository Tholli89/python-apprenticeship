def count_words_in_file(filename):
    counts = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    return counts


if __name__ == "__main__":
    result = count_words_in_file("sample.txt")
    print(result)