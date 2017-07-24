from gascore import *

def test_choices():
    assert choices('1') == 'Refilled Tanks'
    assert gas_name('3') == 'Premium'