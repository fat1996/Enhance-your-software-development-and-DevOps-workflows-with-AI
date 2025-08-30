# example for role based prompting
def average(nums):
    total = 0
    for n in nums:
        total = n  # BUG: overwriting instead of accumulating
    return total / len(nums)


# example of messy, hard to read code
from decimal import Decimal

def compute_total(items, coupon=None, tax_rate=Decimal("0.13")):
    # items: list of {"price": "12.99", "qty": 2}
    total = Decimal("0")
    for i in range(len(items)):
        p = Decimal(str(items[i]["price"]))
        q = items[i].get("qty")
        if q is None:
            q = 1
        total = total + (p * q)
    if coupon:
        if coupon["type"] == "percent":
            total = total - (total * Decimal(str(coupon["value"])) / Decimal("100"))
        else:
            if coupon["type"] == "amount":
                total = total - Decimal(str(coupon["value"]))
    tax = total * tax_rate
    total = total + tax
    return total.quantize(Decimal("0.01"))
