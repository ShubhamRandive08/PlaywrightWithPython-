def test_assert():
    assert 'Hello' != 'Helloo'
    inputs = "Shubham"
    outputs = "Shubham"
    input_data = 'Shubham is QA Engineer'

    print("Assert Code starting")
    assert inputs == outputs, 'Both strings are matched'
    assert "lhg" in input_data
    assert False, 'Default failed'
    print("Assert Code ending")




