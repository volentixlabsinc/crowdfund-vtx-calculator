import pytest
from business.price_calculator import compute_price

@pytest.mark.parametrize('tokencount, price', [
  (0, 2590),
  (112160, 2590),
  (112161, 2591),
  (224321, 2591),
  (224322, 2592),
  (281520000, 5099),
  (281524109, 5099),
  (281524110, 5100),
])
def test_price_calculations(tokencount, price):
    rprice = compute_price(tokencount)
    assert rprice == price
