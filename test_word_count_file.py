from word_count_in_file import count_words_in_file

def test_count_words_in_file():
    result = count_words_in_file("sample.txt")

    # Very simple checks
    print("Result:", result)

    if result.get("hello") ==2:
        print("PASS: 'hello' count is 2")

    else:
        print("FAIL: expected 'hello' count to be 2")

    if result.get("world") == 3:
        print("PASS: 'world' count is 3")

    else:
        print("FAIL: expected 'world' count to be 3")

if __name__ == "__main__":
    test_count_words_in_file()