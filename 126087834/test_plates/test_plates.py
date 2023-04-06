from plates import is_valid

def main():
    test_start()
    test_length()
    test_numbers()
    test_zero()
    test_punc()

def test_start():
    assert is_valid('ABCDEF') == True
    assert is_valid('1ABCDE') == False
    assert is_valid('A3CDEF') == False
    assert is_valid('63CDEF') == False

def test_length():
    assert is_valid('ABCDEF') == True
    assert is_valid('ABCDE') == True
    assert is_valid('ABC') == True
    assert is_valid('AB') == True
    assert is_valid('A') == False

def test_numbers():
    assert is_valid('ABC123') == True
    assert is_valid('ABCD12') == True
    assert is_valid('ABCDE1') == True
    assert is_valid('AB23EF') == False
    assert is_valid('ABC23F') == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

def test_zero():
    assert is_valid('ABC102') == True
    assert is_valid('CS50') == True
    assert is_valid('ABC012') == False
    assert is_valid('ABCD01') == False

def test_punc():
    assert is_valid('ABC,23') == False
    assert is_valid('ABC 23') == False
    assert is_valid('ABC.12') == False
    assert is_valid('AB:12') == False
    assert is_valid('AB/45') == False

if __name__ == "__main__":
    main()

