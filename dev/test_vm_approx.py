from vm import approx_equal

def test_approx_equal():
    assert approx_equal(4.5, 4.6) == False
    assert approx_equal(4.5, 4.50000000005) == True