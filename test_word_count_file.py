from word_count_in_file import count_words_in_file

def test_count_words_in_file():
    result = count_words_in_file("sample.txt")

    assert result["hello"] == 2
    assert result["world"] == 4
    assert result["python"] == 1
    assert result["is"] == 1