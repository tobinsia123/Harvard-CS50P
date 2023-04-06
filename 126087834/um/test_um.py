from um import count

def test_count():
    assert count("no Um! hi um? um. who") == 3
    assert count(", uM, ! mU") == 1
    assert count("wHat, um, yea") == 1
    assert count(" what! Um???") == 1
    assert count("UM who Is tHat") == 1
    assert count("UMM what!") == 0
    assert count("Hey UM?") == 1
    assert count("WHat U.m?") == 0
    assert count("WHo Is tHat U m!") == 0