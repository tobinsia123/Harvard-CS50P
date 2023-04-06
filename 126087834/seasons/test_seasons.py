from seasons import check_birthday

def main():
    test_check()

def test_check():
    assert check_birthday('1998-07-03') == ("1998", "07", "03")
    assert check_birthday('1998-7-3') == None
    assert check_birthday('July 3, 1998') == None

if __name__ == "__main__":
    main()