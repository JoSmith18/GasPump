from gascore import *

def test_choices():
    assert choices('1') == 'Refilled Tanks'

def test_gasname():
    assert gas_name('3') == 'Premium'

def test_refill():
    assert refill([['1', 'Regular', 1, 2.13]]) == 'Num, Type, Gallons, Price\n1, Regular, 5000.00, 2.13'

def test_revenue():
    assert revenue([['1', 'Regular', 1, 2.13]]) == 2.13
    assert revenue([['2', 'Midgrade', 2, 4.46],['1', 'Regular', 1, 2.13]]) == 6.59

