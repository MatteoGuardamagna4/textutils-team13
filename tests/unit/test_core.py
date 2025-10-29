import textutils.core as c

def test_camel_to_snake_simple():
    assert c.camel_to_snake("camelCase") == "camel_case"

