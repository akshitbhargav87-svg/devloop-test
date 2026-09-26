def calculate_discount(total, coupon_rate=None):
    if coupon_rate is None:
        return total
    return total * coupon_rate
