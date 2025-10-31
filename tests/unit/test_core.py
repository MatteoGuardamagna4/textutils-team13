import textutils as c 

def test_slugify_basic():
    assert c.slugify("Hello World") == "hello-world"
    assert c.slugify("Python-Test Driven Development") == "python-test-driven-development"

