def greeting(name: str) -> int:
    return ("Hello" + name)

def test_greeting():
    assert "Hello"+"nannan"== greeting("nannan")