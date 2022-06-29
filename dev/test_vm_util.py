from vm import CodeNumber, Triple, code_number_of, triple_of

def test_code_number_and_triple():
    assert code_number_of(Triple(21, 20, 29)) == CodeNumber(5, 2)
    assert triple_of(CodeNumber(5, 2)) == Triple(21, 20, 29)
    assert triple_of(CodeNumber(6)) == Triple(35, 12, 37)
    assert triple_of(CodeNumber(10, 3)) == Triple(91, 60, 109)
    assert triple_of(CodeNumber(-6, -4)) == Triple(5, 12, 13)