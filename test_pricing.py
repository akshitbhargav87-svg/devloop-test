from pricing import calculate_discount


def test_coupon_discount():
    result = calculate_discount(100, 0.25)
    assert result == 75


def test_no_coupon():
    result = calculate_discount(100)
    assert result == 100
