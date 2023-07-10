from hello import hello

def test_default():
    assert hello("BrandAnn") == "hello, BrandAnn"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

# def test_argument():
    # for name in ["Hermione", "Harry", "Ron"]:
        # assert hello(name) == f"hello, {name}"