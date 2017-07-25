from gascore import *

def test_choices():
    assert choices('1') == 'Refilled Tanks'
    assert choices('2') == 'Checked Revenue'
    assert choices('3') == 'Opened Log'
    assert choices('4') == 'Looked At Tank'

def test_gasname():
    assert gas_name('1') == 'Regular'
    assert gas_name('2') == 'Midgrade'
    assert gas_name('3') == 'Premium'
    assert gas_name('4') == 'Error Start Over'

def test_refill():
    assert refill([['1', 'Regular', 1, 2.13]]) == 'Num, Type, Gallons, Price\n1, Regular, 5000.00, 2.13'

def test_revenue():
    assert revenue([['1', 'Regular', 1, 2.13]]) == 2.13
    assert revenue([['2', 'Midgrade', 2, 4.46],['1', 'Regular', 1, 2.13]]) == 6.59

def test_prepay():
    assert add_prepay( 12, '1', [
    ['Regular', 2.08],
    ['Midgrade', 2.23],
    ['Premium', 2.36]  
]) == [5.77, 12]

def test_payafter():
    assert add_payafter('2', [
    ['Regular', 2.08],
    ['Midgrade', 2.23],
    ['Premium', 2.36]  
], 12) == [12, 26.759999999999998]

def test_write_message():
    assert write_message([], 1, 23) == 'Num, Type, Gallons, Price'
    assert write_message([['1', 'Regular', 4994.23, 2.13]], 1, [25,20]) == 'Num, Type, Gallons, Price\n1, Regular, 4994.23, 2.13'
