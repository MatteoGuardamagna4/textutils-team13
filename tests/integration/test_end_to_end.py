import textutils.core as c

def test_camel_to_snake_pipeline():
    text = "camelCaseTest"
    result = c.camel_to_snake(text)
    assert result == "camel_case_test"
